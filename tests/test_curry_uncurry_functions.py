import pytest

from src.curry_uncurry_functions.curry import curry
from src.curry_uncurry_functions.uncurry import uncurry


def test_curry_basic(add_two):
    """Базовый тест функции curry"""
    curried = curry(add_two, 2)
    assert curried(5)(10) == 15
    assert curried(3)(7) == 10


def test_curry_multiple_args(multiply_three):
    """Тест функции каррирования для исходной функции от трех аргументов"""
    curried = curry(multiply_three, 3)
    assert curried(2)(3)(4) == 24
    assert curried(0)(5)(10) == 0
    assert curried(-2)(3)(4) == -24


def test_curry_zero_arity(constant_func):
    """Тест функции каррирования для исходной функции без аргументов"""
    curried = curry(constant_func, 0)
    assert curried() == 42


def test_curry_with_errors(add_two):
    """Тест обнаружения исключений для функции каррирования"""
    with pytest.raises(ValueError):
        curry(add_two, -1)

    with pytest.raises(TypeError):
        curry(42, 2)


def test_uncurry_basic(add_two):
    """Базовый тест обратной функции каррирования"""
    curried = curry(add_two, 2)
    uncurried = uncurry(curried, 2)

    assert uncurried(5, 10) == 15
    assert uncurried(3, 7) == 10


def test_uncurry_with_errors(add_two):
    """Тест обнаружения исключения для обратной функции"""
    curried = curry(add_two, 2)
    uncurried = uncurry(curried, 2)

    with pytest.raises(TypeError):
        uncurried(1)

    with pytest.raises(TypeError):
        uncurried(1, 2, 3)


def test_curry_uncurry_round_trip():
    """Тест полного цикла преобразований"""

    def custom_func(x, y, z):
        return x * 100 + y * 10 + z

    curried = curry(custom_func, 3)
    uncurried = uncurry(curried, 3)

    assert curried(1)(2)(3) == uncurried(1, 2, 3) == 123


def test_property_based_random(random_int_triple, sum_three):
    """Тест полного цикла преобразований на случайных данных"""
    a, b, c = random_int_triple

    curried = curry(sum_three, 3)
    uncurried = uncurry(curried, 3)

    assert curried(a)(b)(c) == uncurried(a, b, c) == a + b + c


def test_edge_cases(identity):
    """Тест краевых случаев"""
    # Функция с одним аргументом
    curried_identity = curry(identity, 1)
    assert curried_identity(5) == 5

    # Функция с большой арностью
    def large_func(a, b, c, d, e):
        return a + b + c + d + e

    curried_large = curry(large_func, 5)
    assert curried_large(1)(2)(3)(4)(5) == 15

    # Частичное применение (исходная функция и оно)
    def partial_func(a, b, c):
        return a + b + c

    curried_partial = curry(partial_func, 3)
    partially_applied = curried_partial(10)
    assert partially_applied(20)(30) == 60


def test_integration_multiple_functions(add_two, multiply_three, sum_three):
    """Большой тест с несколькими функциями"""
    test_cases = [
        (add_two, 2, [(5, 10), (3, 7), (-2, 2)]),
        (multiply_three, 3, [(2, 3, 4), (1, 5, 2), (0, 10, 5)]),
        (sum_three, 3, [(1, 2, 3), (10, 20, 30), (-5, 0, 5)]),
    ]

    for func, arity, test_values in test_cases:
        curried = curry(func, arity)
        uncurried = uncurry(curried, arity)

        for args in test_values:
            curried_result = curried
            for arg in args:
                curried_result = curried_result(arg)

            uncurried_result = uncurried(*args)

            assert curried_result == uncurried_result


def test_curry_incorrect_arity_immediate_error_with_fixtures(
    add_two, multiply_three, constant_func, identity
):
    """Тест проверки ошибок арности с использованием фикстур"""

    with pytest.raises(ValueError):
        curry(add_two, 3)  # add_two имеет 2 параметра

    with pytest.raises(ValueError):
        curry(multiply_three, 5)  # multiply_three имеет 3 параметра

    with pytest.raises(ValueError):
        curry(add_two, 1)

    with pytest.raises(ValueError):
        curry(multiply_three, 2)

    with pytest.raises(ValueError):
        curry(add_two, 0)

    with pytest.raises(ValueError):
        curry(identity, 0)  # identity имеет 1 параметр

    with pytest.raises(ValueError):
        curry(constant_func, 1)
