"""
Описание: Этот модуль содержит три реализации алгоритма
для подсчета количества корректных расстановок N ферзей на шахматной доске размером N x N.

Ферзь может перемещаться по горизонтали, вертикали и диагонали.
Расстановка считается корректной, если ни один ферзь не атакует другого.

Реализации алгоритма:
1. Переборная через генерацию всех перестановок
2. Рекурсивная с отслеживанием занятых столбцов и диагоналей
3. Оптимизированная рекурсивный с использованием битовых масок
"""

import itertools


def brute_force_solution(board_size: int) -> int:
    """
    Переборное решение через генерацию всех перестановок.

    Алгоритм:
    1. Генерируем все перестановки чисел от 0 до N-1, где индекс — строка,
       а значение — столбец ферзя.
    2. Для каждой перестановки проверяем, не находятся ли какие-либо два ферзя
       на одной диагонали (на одной строке или столбце они гарантированно не
       находятся из-за структуры перестановки).
    3. Считаем количество безопасных расстановок.


    Принимаем:
        board_size (int): Размер доски и количество ферзей.

    Возвращаем:
        int: Количество безопасных расстановок.
    """
    safe_placements_count = 0

    # Генерируем все возможные расстановки ферзей по столбцам
    for column_permutation in itertools.permutations(range(board_size)):
        is_safe = True

        # Проверяем все пары ферзей на конфликт по диагоналям
        for first_row in range(board_size - 1):
            for second_row in range(first_row + 1, board_size):
                # Два ферзя на одной диагонали, если разность строк равна разности столбцов (по модулю)
                if abs(first_row - second_row) == abs(
                    column_permutation[first_row] - column_permutation[second_row]
                ):
                    is_safe = False
                    break
            if not is_safe:
                break

        # Если ни один ферзь не атакует другого, увеличиваем счетчик
        if is_safe:
            safe_placements_count += 1

    return safe_placements_count


def recursive_solution(board_size: int) -> int:
    """
    Рекурсивное решение с отслеживанием занятых линий (столбцы, диагонали).

    Алгоритм:
    Размещаем ферзей по одному на каждой строке, начиная с первой.
    Для каждой строки перебираем все столбцы и проверяем, не атакует ли
    текущая позиция уже размещенных ферзей по вертикали или диагоналям.

    Для ускорения проверок используем множества занятых позиций:
        - Занятые столбцы
        - Занятые восходящие диагонали (row - col)
        - Занятые нисходящие диагонали (row + col)

    Принимаем:
        board_size (int): Размер доски и количество ферзей.

    Возвращаем:
        int: Количество безопасных расстановок.
    """
    # Множества для отслеживания занятых линий
    occupied_columns = set()  # множество занятых столбцов
    occupied_main_diagonals = set()  # множество занятых главных диагоналей, определяются постоянной разностью row - col
    occupied_secondary_diagonals = (
        set()
    )  # множество занятых побочных диагоналей, определяются постоянной суммой row + col

    safe_placements_count = 0

    def place_queen_in_row(current_row: int) -> None:
        """
        Рекурсивно размещает ферзя в текущей строке.

        Принимаем:
            current_row (int): Текущая строка для размещения ферзя (индексация начинается с 0).
        """
        nonlocal safe_placements_count

        # Базовый случай: все ферзи успешно размещены
        if current_row == board_size:
            safe_placements_count += 1
            return

        # Перебираем все возможные столбцы в текущей строке
        for column in range(board_size):
            # Проверяем, безопасна ли текущая позиция
            is_column_free = column not in occupied_columns
            is_main_diag_free = (current_row - column) not in occupied_main_diagonals
            is_sec_diag_free = (
                current_row + column
            ) not in occupied_secondary_diagonals

            if is_column_free and is_main_diag_free and is_sec_diag_free:
                # Занимаем линии, которые контролирует этот ферзь
                occupied_columns.add(column)
                occupied_main_diagonals.add(current_row - column)
                occupied_secondary_diagonals.add(current_row + column)

                # Рекурсивно размещаем следующего ферзя
                place_queen_in_row(current_row + 1)

                # Освобождаем линии для backtracking (возврата)
                occupied_columns.remove(column)
                occupied_main_diagonals.remove(current_row - column)
                occupied_secondary_diagonals.remove(current_row + column)

    # Начинаем размещение с первой строки
    place_queen_in_row(current_row=0)
    return safe_placements_count


def bitmask_solution(board_size: int) -> int:
    """
    Оптимизированное решение с использованием битовых масок.

    Алгоритм:
    Использует целые числа как битовые массивы для представления занятых позиций.
    Каждый бит представляет конкретный столбец. Это позволяет выполнять операции
    проверки и установки за O(1) с помощью битовых операций.

    Преимущества:
        - Экономия памяти (3 целых числа вместо 3 множеств)
        - Высокая скорость битовых операций
        - Автоматический контроль за пределами доски через битовые сдвиги

    Принимаем:
        board_size (int): Размер доски и количество ферзей.

    Возвращаем:
        int: Количество безопасных расстановок.
    """
    safe_placements_count = 0

    # Маска всех допустимых позиций: N младших битов установлены в 1
    full_mask = (1 << board_size) - 1

    def place_queens_with_bitmask(
        columns_mask: int, main_diagonals_mask: int, secondary_diagonals_mask: int
    ) -> None:
        """
        Рекурсивно размещает ферзей с использованием битовых масок.

        Принимаем:
            columns_mask (int): Биты установлены для занятых столбцов.
            main_diagonals_mask (int): Биты установлены для занятых главных диагоналей.
            secondary_diagonals_mask (int): Биты установлены для занятых побочных диагоналей.
        """
        nonlocal safe_placements_count

        # Все ферзи размещены, если заняты все столбцы
        if columns_mask == full_mask:
            safe_placements_count += 1
            return

        # Определяем доступные позиции в текущей строке:
        # Берем все столбцы (~ инвертирует маску), но ограничиваем размером доски
        free_positions = full_mask & ~(
            columns_mask | secondary_diagonals_mask | main_diagonals_mask
        )

        # Последовательно занимаем каждую доступную позицию
        while free_positions:
            # Выбираем младший установленный бит (самую правую свободную позицию)
            current_position = free_positions & -free_positions

            # Рекурсивно размещаем оставшихся ферзей:
            # 1. columns_mask | current_position — занимаем текущий столбец
            # 2. (secondary_diagonals_mask | current_position) >> 1 — сдвиг главной диагонали для следующей строки
            # 3. (main_diagonals_mask | current_position) << 1 — сдвиг побочной диагонали для следующей строки
            place_queens_with_bitmask(
                columns_mask | current_position,
                (main_diagonals_mask | current_position) << 1,
                (secondary_diagonals_mask | current_position) >> 1,
            )

            # Убираем текущую позицию из свободных для следующей итерации
            free_positions ^= current_position

    # Инициализируем рекурсию с пустой доской
    place_queens_with_bitmask(0, 0, 0)
    return safe_placements_count
