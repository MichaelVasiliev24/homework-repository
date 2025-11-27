def brute_force_solution(N):
    import itertools

    counter = 0
    for perm_of_columns in itertools.permutations(range(N)):
        flag = True
        for i_row in range(N - 1):
            for j_row in range(i_row + 1, N):
                if abs(i_row - j_row) == abs(
                    perm_of_columns[i_row] - perm_of_columns[j_row]
                ):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            counter += 1
    return counter


def recursive_solution(N):
    occupied_columns, occupied_main_diagonals, occupied_secondary_diagonals = (
        set(),
        set(),
        set(),
    )
    counter = 0

    def recursive_function_for_rows(current_row):
        nonlocal counter

        if current_row == N:
            counter += 1
            return

        for i_column in range(N):
            if (
                i_column not in occupied_columns
                and (current_row - i_column) not in occupied_main_diagonals
                and (current_row + i_column) not in occupied_secondary_diagonals
            ):
                occupied_columns.add(i_column)
                occupied_main_diagonals.add(current_row - i_column)
                occupied_secondary_diagonals.add(current_row + i_column)

                recursive_function_for_rows(current_row + 1)

                occupied_columns.remove(i_column)
                occupied_main_diagonals.remove(current_row - i_column)
                occupied_secondary_diagonals.remove(current_row + i_column)
        return

    recursive_function_for_rows(current_row=0)
    return counter


def bitmask_solution(N):
    counter = 0
    initial_mask = (1 << N) - 1

    def recursive_function_bitmask_solution(
        columns, secondary_diagonals, main_diagonals
    ):
        nonlocal counter

        if columns == initial_mask:
            counter += 1
            return

        available_positions = initial_mask & ~(
            columns | secondary_diagonals | main_diagonals
        )

        while available_positions:
            current_pos = available_positions & -available_positions
            recursive_function_bitmask_solution(
                (columns | current_pos),
                (secondary_diagonals | current_pos) >> 1,
                (main_diagonals | current_pos) << 1,
            )
            available_positions ^= current_pos
        return

    recursive_function_bitmask_solution(0, 0, 0)
    return counter