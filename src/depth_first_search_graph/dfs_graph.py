class Graph:
    """
    Класс для представления неориентированного непомеченного графа
    Использует список смежности для хранения рёбер
    """

    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        # Список смежности, для каждой вершины список соседей
        self._adjacency_list = [[] for _ in range(vertices_count)]

    def add_edge(self, u, v):
        """Добавить неориентированное ребро между вершинами"""
        if u < 0 or u >= self.vertices_count or v < 0 or v >= self.vertices_count:
            raise ValueError("Vertex index out of range")

        # Добавляем "v" в список соседей "u", а также и наоборот (неориентированный граф)
        self._adjacency_list[u].append(v)
        self._adjacency_list[v].append(u)

    def dfs(self, start_vertex):
        """
        Алгоритм обхода графа в глубину из заданной вершины
        Метод возвращает список посещённых вершин
        В несвязном графе возвращает только вершины из компоненты связности start_vertex
        """
        if start_vertex < 0 or start_vertex >= self.vertices_count:
            raise ValueError("Start vertex index out of range")

        visited = [False] * self.vertices_count
        stack = [start_vertex]
        result = []

        # Итеративная реализация DFS с использованием стека
        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)

                # Добавляем соседей в исходном порядке
                for neighbor in self._adjacency_list[vertex]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

        return result

    def __iter__(self):
        """
        Превращает граф в итерируемый (в порядке обхода DFS)
        Возвращает итератор, который обходит ВСЕ вершины графа,
        В несвязном графе - по одной компоненте связности за раз
        """
        return self.DFSIterator(self)

    class DFSIterator:
        """
        Внутренний класс-итератор для обхода графа в глубину.
        Обрабатывает несвязные графы, обходя все компоненты связности.
        """

        def __init__(self, graph: "Graph"):
            self.graph = graph

            # Инициализируем состояние DFS
            self.visited = [False] * graph.vertices_count
            self.stack = []
            self.current_start = 0  # Начинаем поиск с вершины 0

            # Находим первую вершину
            self._next_value = None
            self.find_next()

        def __iter__(self):
            """Возвращает самого себя в качестве итератора"""
            return self

        def find_next(self):
            """Поиск следующей вершины в порядке DFS с учётом несвязных графов"""
            # Ищем следующую вершину, пока не найдем или не обойдем все
            while self._next_value is None:
                if self.stack:
                    vertex = self.stack.pop()

                    if not self.visited[vertex]:
                        self.visited[vertex] = True
                        self._next_value = vertex

                        # Добавляем соседей в стек в исходном порядке
                        for neighbor in self.graph._adjacency_list[vertex]:
                            if not self.visited[neighbor]:
                                self.stack.append(neighbor)
                        break
                else:
                    found = False
                    for i in range(self.current_start, self.graph.vertices_count):
                        if not self.visited[i]:
                            self.stack.append(i)
                            self.current_start = i + 1
                            found = True
                            break
                    if not found:
                        break

        def __next__(self) -> int:
            """
            Возвращает следующую вершину в порядке DFS
            Поднимает StopIteration, когда все вершины посещены
            """
            if self._next_value is None:
                raise StopIteration

            result = self._next_value
            self._next_value = None
            self.find_next()  # Ищем следующую вершину
            return result
