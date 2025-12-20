import pytest

from src.depth_first_search_graph.dfs_graph import Graph


class TestDFSMethod:
    """Класс тестов для метода обхода в глубину"""

    def test_dfs_simple_graph(self, simple_graph):
        """DFS посещает все вершины связного графа"""
        result = simple_graph.dfs(0)
        assert sorted(result) == [0, 1, 2, 3, 4]
        assert result[0] == 0

    def test_dfs_disconnected_graph(self, disconnected_graph):
        """DFS возвращает только компоненту связности стартовой вершины"""
        result = disconnected_graph.dfs(0)
        assert sorted(result) == [0, 1, 2]

        result2 = disconnected_graph.dfs(3)
        assert sorted(result2) == [3, 4, 5]

    def test_dfs_empty_graph(self, empty_graph):
        """В графе без рёбер каждая вершина - отдельная компонента"""
        assert empty_graph.dfs(0) == [0]
        assert empty_graph.dfs(1) == [1]
        assert empty_graph.dfs(2) == [2]

    def test_dfs_invalid_vertex(self):
        """Проверка корректности входных параметров"""
        g = Graph(3)
        with pytest.raises(ValueError, match="Start vertex index out of range"):
            g.dfs(-1)

        with pytest.raises(ValueError, match="Start vertex index out of range"):
            g.dfs(5)

    def test_dfs_add_edge_validation(self):
        """Проверка корректности при добавлении рёбер"""
        g = Graph(3)
        g.add_edge(0, 1)

        with pytest.raises(ValueError, match="Vertex index out of range"):
            g.add_edge(-1, 0)

        with pytest.raises(ValueError, match="Vertex index out of range"):
            g.add_edge(0, 5)

    @pytest.mark.parametrize("start_vertex", [0, 1, 2, 3])
    def test_dfs_cycle_graph(self, cycle_graph, start_vertex):
        """Параметризованный тест: DFS из любой вершины цикла посещает все вершины"""
        result = cycle_graph.dfs(start_vertex)
        assert sorted(result) == [0, 1, 2, 3]


class TestDFSIterator:
    """Класс тестов для итератора графа"""

    def test_iterator_simple_graph(self, simple_graph):
        """Итератор обходит все вершины связного графа"""
        vertices = list(simple_graph)
        assert sorted(vertices) == [0, 1, 2, 3, 4]
        assert len(set(vertices)) == 5

    def test_iterator_disconnected_graph(self, disconnected_graph):
        """Итератор обходит все вершины несвязного графа"""
        vertices = list(disconnected_graph)
        assert sorted(vertices) == [0, 1, 2, 3, 4, 5]
        assert len(vertices) == 6

    def test_iterator_empty_graph(self, empty_graph):
        """Итератор для графа без рёбер"""
        vertices = list(empty_graph)
        assert sorted(vertices) == [0, 1, 2]

    def test_iterator_multiple_iterations(self, simple_graph):
        """Многократные итерации и одинаковый результат"""
        first = list(simple_graph)
        second = list(simple_graph)
        assert first == second

    def test_iterator_manual_iteration(self, disconnected_graph):
        """Ручное использование итератора"""
        iterator = iter(disconnected_graph)

        first_three = [next(iterator) for _ in range(3)]
        assert set(first_three) == {0, 1, 2}

        remaining = list(iterator)
        assert set(remaining) == {3, 4, 5}

        with pytest.raises(StopIteration):
            next(iterator)


class TestPropertyBased:
    """Класс property-based тестов"""

    def test_iterator_completeness_property(self):
        """Итератор всегда посещает все вершины ровно один раз"""
        import random

        for _ in range(5):
            n = random.randint(5, 10)
            g = Graph(n)

            for _ in range(random.randint(0, n * 2)):
                u = random.randint(0, n - 1)
                v = random.randint(0, n - 1)
                if u != v:
                    g.add_edge(u, v)

            vertices = list(g)
            assert set(vertices) == set(range(n))
            assert len(vertices) == n

    def test_dfs_component_property(self):
        """DFS всегда возвращает вершины из одной компоненты связности"""
        import random

        for _ in range(5):
            n = random.randint(4, 8)
            g = Graph(n)

            split = random.randint(1, n - 2)

            for i in range(split - 1):
                g.add_edge(i, i + 1)

            for i in range(split, n - 1):
                g.add_edge(i, i + 1)

            start = random.randint(0, n - 1)
            result = g.dfs(start)

            if start < split:
                assert all(v < split for v in result)
            else:
                assert all(v >= split for v in result)


class TestEdgeCases:
    """Класс тестов краевых случаев"""

    def test_graph_zero_vertices(self):
        """Граф с 0 вершин"""
        g = Graph(0)
        assert list(g) == []

        with pytest.raises(ValueError):
            g.dfs(0)

    def test_graph_single_vertex(self):
        """Граф с одной вершиной"""
        g = Graph(1)
        assert g.dfs(0) == [0]
        assert list(g) == [0]

    def test_self_loop_handling(self):
        """Образование петель"""
        g = Graph(3)
        g.add_edge(0, 0)
        g.add_edge(0, 1)

        result = g.dfs(0)
        assert 0 in result and 1 in result

    def test_duplicate_edges(self):
        """Дублирующиеся рёбра"""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(0, 1)

        result = g.dfs(0)
        assert sorted(result) == [0, 1]
