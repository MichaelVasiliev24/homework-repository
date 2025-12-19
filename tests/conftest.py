import random

import pytest


@pytest.fixture
def random_list():
    """Cлучайный список чисел для тестов"""
    n = random.randint(5, 20)
    return [random.randint(-100, 100) for _ in range(n)]


@pytest.fixture
def empty_list():
    """Пустой список"""
    return []


@pytest.fixture
def single_element_list():
    """Список из одного элемента"""
    return [42]


@pytest.fixture
def sorted_list():
    """Уже отсортированный список"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def reversed_list():
    """Список, отсортированного в обратном порядке"""
    return [5, 4, 3, 2, 1]


@pytest.fixture
def list_with_duplicates():
    """Список с дубликатами"""
    return [3, 1, 3, 2, 1, 2]


@pytest.fixture
def add_two():
    """Функция сложения двух чисел"""

    def func(a, b):
        return a + b

    return func


@pytest.fixture
def sum_three():
    """Функция сложения трех чисел"""

    def func(x, y, z):
        return x + y + z

    return func


@pytest.fixture
def multiply_three():
    """Функция умножения трех чисел"""

    def func(x, y, z):
        return x * y * z

    return func


@pytest.fixture
def constant_func():
    """Функция без аргументов"""

    def func():
        return 42

    return func


@pytest.fixture
def identity():
    """Функция идентичности"""

    def func(x):
        return x

    return func


@pytest.fixture
def random_int_triple():
    """Тройка случайных целых чисел"""
    return (random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5))
