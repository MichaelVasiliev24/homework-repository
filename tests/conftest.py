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
