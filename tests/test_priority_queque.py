import pytest

from src.priority_queque import PriorityQueue


@pytest.fixture
def empty_queue():
    """Подготовка пустой очереди"""
    return PriorityQueue()


@pytest.fixture
def sample_queue():
    """Подготовка очереди с тестовыми данными"""
    pq = PriorityQueue()
    pq.insert("C", 30)
    pq.insert("A", 10)
    pq.insert("B", 20)
    return pq


class TestBasicOperations:
    """Класс тестов базовых операций с очередью"""

    def test_empty_queue(self, empty_queue):
        """Тест: пустая очередь"""
        assert empty_queue.is_empty() is True
        assert empty_queue.get_min() is None
        assert empty_queue.extract_min() is None

    def test_insert_and_get_min(self, empty_queue):
        """Тест: вставка и получение минимума"""
        node = empty_queue.insert("test", 5)
        assert empty_queue.is_empty() is False
        assert empty_queue.get_min() == ("test", 5)
        assert node.value == "test"
        assert node.priority == 5

    def test_extract_min_ordering(self, sample_queue):
        """Тест: извлечение минимумов в правильном порядке"""
        assert sample_queue.extract_min() == ("A", 10)
        assert sample_queue.extract_min() == ("B", 20)
        assert sample_queue.extract_min() == ("C", 30)
        assert sample_queue.is_empty() is True


class TestDecreaseKey:
    """Класс тестов операций уменьшения приоритета"""

    def test_decrease_key_basic(self):
        """Базовый тест"""
        pq = PriorityQueue()
        node_b = pq.insert("B", 20)
        pq.insert("A", 10)

        pq.decrease_key(node_b, 5)

        assert pq.get_min() == ("B", 5)
        assert pq.extract_min() == ("B", 5)
        assert pq.extract_min() == ("A", 10)

    def test_decrease_key_error(self):
        """Тест: ошибка при увеличении приоритета"""
        pq = PriorityQueue()
        node = pq.insert("test", 10)

        with pytest.raises(ValueError, match="Новый приоритет должен быть меньше"):
            pq.decrease_key(node, 15)


class TestDelete:
    """Класс тестов операций удаления"""

    def test_delete_basic(self):
        pq = PriorityQueue()
        node_b = pq.insert("B", 20)
        pq.insert("A", 10)
        pq.insert("C", 30)

        deleted = pq.delete(node_b)

        # Проверяем только значение, т.к. приоритет изменен
        assert deleted[0] == "B"  # Значение правильное
        # Проверяем, что очередь работает дальше
        assert pq.extract_min()[0] == "A"
        assert pq.extract_min()[0] == "C"


class TestEdgeCases:
    """Класс тестов граничных случаев"""

    @pytest.mark.parametrize(
        "values, priorities, expected_min",
        [
            ([1, 2, 3], [3, 2, 1], (3, 1)),  # Минимальный в конце
            (["x", "y", "z"], [5, 1, 3], ("y", 1)),  # Минимальный в середине
        ],
    )
    def test_parametrized_insert(self, values, priorities, expected_min):
        """Тест вставки (с параметрами)"""
        pq = PriorityQueue()
        for v, p in zip(values, priorities):
            pq.insert(v, p)

        assert pq.get_min() == expected_min
        assert pq.extract_min() == expected_min

    def test_equal_priorities(self):
        """Тест: одинаковые приоритеты"""
        pq = PriorityQueue()
        pq.insert("A", 10)
        pq.insert("B", 10)

        min_val = pq.extract_min()
        assert min_val[1] == 10
        assert pq.extract_min()[1] == 10
        assert pq.is_empty() is True

    def test_reinsert_after_empty(self):
        """Тест: повторная вставка после опустошения"""
        pq = PriorityQueue()

        # Первый раз
        pq.insert("first", 5)
        pq.extract_min()

        # Второй раз
        pq.insert("second", 3)
        assert pq.extract_min() == ("second", 3)
        assert pq.is_empty() is True
