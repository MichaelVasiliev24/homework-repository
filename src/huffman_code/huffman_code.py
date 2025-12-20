"""
Реализация алгоритма Хаффмана для кодирования и декодирования
"""

import heapq

from typing import Any


class Node:
    def __init__(self, char: str | None, freq: int) -> None:
        self.char = char
        self.freq = freq
        self.left: Node | None = None
        self.right: Node | None = None

    def __lt__(self, other: Any) -> bool:
        if not hasattr(other, "freq"):
            return NotImplemented
        return self.freq < other.freq


def count_frequencies(text: str) -> dict[str, int]:
    """Подсчёт количества вхождений каждого символа в тексте"""
    if not text:
        return {}

    freq: dict[str, int] = {}
    for char in text:
        # Пропускаем пустые строки (в обычном тексте их нет)
        if char:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def build_tree(text: str) -> Node | None:
    """Построение дерева Хаффмана"""
    if not text:
        return None

    freq = count_frequencies(text)

    # Если после фильтрации нет символов
    if not freq:
        return None

    # Если текст состоит только из одного уникального символа
    if len(freq) == 1:
        char = list(freq.keys())[0]
        return Node(char, freq[char])

    heap: list[Node] = []
    for char, count in freq.items():
        heapq.heappush(heap, Node(char, count))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0] if heap else None


def make_codes(root: Node | None) -> dict[str, str]:
    """Создание таблицы кодов Хаффмана"""
    if root is None:
        return {}

    codes: dict[str, str] = {}

    def walk(node: Node | None, code: str) -> None:
        if node is None:
            return

        if node.char is not None:
            if node.char:
                codes[node.char] = code
            return

        walk(node.left, code + "0")
        walk(node.right, code + "1")

    walk(root, "")
    return codes


def encode(text: str):
    """Кодирование текста алгоритмом Хаффмана"""
    if not text:
        return "", {}

    if not isinstance(text, str):
        raise TypeError(f"Ожидается строка, получен {type(text).__name__}")

    root = build_tree(text)

    if root is None:
        return "", {}

    # Особый случай - один уникальный символ
    codes = make_codes(root) if root.char is None else {root.char: "0"}
    if not codes:
        return "", {}

    # Проверяем, что все символы текста есть в таблице кодов
    missing_chars = set(text) - set(codes.keys())
    if missing_chars:
        raise ValueError(f"Символы отсутствуют в таблице кодов: {missing_chars}")

    encoded_parts: list[str] = []
    for char in text:
        encoded_parts.append(codes[char])

    encoded = "".join(encoded_parts)
    return encoded, codes


def decode(
    encoded: str, codes: dict[str, str], ignore_trailing_bits: bool = False
) -> str:
    """Декодирование строки, закодированной алгоритмом Хаффмана"""
    if not encoded:
        return ""

    if not codes:
        raise ValueError("Таблица кодов не может быть пустой для декодирования")

    # Проверка типов
    if not isinstance(encoded, str):
        raise TypeError(
            f"Ожидается строка для encoded, получен {type(encoded).__name__}"
        )

    if not isinstance(codes, dict):
        raise TypeError(f"Ожидается словарь для codes, получен {type(codes).__name__}")

    # Фильтруем таблицу кодов - удаляем пустые строки и некорректные записи
    filtered_codes: dict[str, str] = {}
    for char, code in codes.items():
        if isinstance(char, str) and isinstance(code, str):
            if char == "":
                continue
            # Проверяем, что код состоит только из 0 и 1
            if not all(bit in "01" for bit in code):
                raise ValueError(
                    f"Некорректный код Хаффмана для символа '{char}': {code}"
                )
            filtered_codes[char] = code
        else:
            # Если типы не строковые, вызываем TypeError
            if not isinstance(char, str):
                raise TypeError(
                    f"Ключ таблицы кодов должен быть строкой, получен {type(char).__name__}"
                )
            if not isinstance(code, str):
                raise TypeError(
                    f"Значение таблицы кодов должно быть строкой, получен {type(code).__name__}"
                )

    if not filtered_codes:
        return ""

    if not all(bit in "01" for bit in encoded):
        raise ValueError("Закодированная строка должна содержать только '0' и '1'")

    reverse_codes: dict[str, str] = {}
    for char, code in filtered_codes.items():
        reverse_codes[code] = char

    result_parts: list[str] = []
    current_code = ""

    for bit in encoded:
        current_code += bit
        if current_code in reverse_codes:
            result_parts.append(reverse_codes[current_code])
            current_code = ""

    # Проверяем остаток
    if (
        current_code
        and not ignore_trailing_bits
        and not all(b == "0" for b in current_code)
    ):
        # Если остаток состоит только из нулей, это может быть padding
        raise ValueError(f"Не удалось декодировать остаток: '{current_code}'")

    return "".join(result_parts)
