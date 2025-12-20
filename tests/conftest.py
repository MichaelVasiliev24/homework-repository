import pytest

from src.depth_first_search_graph.dfs_graph import Graph


@pytest.fixture
def simple_graph():
    """Простой связный граф"""
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    return g


@pytest.fixture
def disconnected_graph():
    """Несвязный граф с двумя компонентами"""
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    return g


@pytest.fixture
def empty_graph():
    """Граф без рёбер"""
    return Graph(3)


@pytest.fixture
def cycle_graph():
    """Граф-цикл"""
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    return g
