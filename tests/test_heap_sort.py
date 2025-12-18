import pytest

from src.heap_sort import heap_sort
from src.other_sorts import bubble_sort, merge_sort


def test_heap_sort_empty(empty_list):
    """Тест для пустого списка"""
    result = heap_sort(empty_list.copy())
    assert result == []


def test_heap_sort_single(single_element_list):
    """Тест для списка из одного элемента"""
    result = heap_sort(single_element_list.copy())
    assert result == [42]


def test_heap_sort_sorted(sorted_list):
    """Тест для уже отсортированного списка"""
    result = heap_sort(sorted_list.copy())
    assert result == [1, 2, 3, 4, 5]


def test_heap_sort_reversed(reversed_list):
    """Тест для списка, отсортированного в обратном порядке"""
    result = heap_sort(reversed_list.copy())
    assert result == [1, 2, 3, 4, 5]


def test_heap_sort_with_duplicates(list_with_duplicates):
    """Тест для списка с дубликатами"""
    result = heap_sort(list_with_duplicates.copy())
    assert result == [1, 1, 2, 2, 3, 3]


def test_heap_sort_random(random_list):
    """Тест для случайного списка"""
    result = heap_sort(random_list.copy())
    expected = sorted(random_list.copy())
    assert result == expected


@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_heap_sort_against_other_sorts(random_list, sort_func):
    """Property-based тесты: сравнение heap_sort с другими сортировками (bubble_sort, merge_sort)"""
    heap_result = heap_sort(random_list.copy())
    other_result = sort_func(random_list.copy())
    assert heap_result == other_result
