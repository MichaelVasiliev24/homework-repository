class Node:  # Узел биномиального дерева
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class PriorityQueue:  # Очередь с приоритетами на основе списка биномиальных деревьев
    MIN_PRIORITY = -(10**18)  # Малая константа, используемая в методе delete

    def __init__(self):
        self.head = None  # Голова для списка корней, отсортированных по степени

    def is_empty(self):
        return self.head is None

    def insert(self, value, priority):
        """Вставка элемента в очередь"""
        new_node = Node(value, priority)
        temp_queue = PriorityQueue()
        temp_queue.head = new_node
        self._merge(temp_queue)
        return new_node

    def get_min(self):
        """Получение минимального элемента, без его удаления"""
        if self.head is None:
            return None

        min_node = self.head
        current = self.head.sibling

        while current:
            if current.priority < min_node.priority:
                min_node = current
            current = current.sibling

        return (min_node.value, min_node.priority)

    def extract_min(self):
        """Извлечение минимального элемента"""
        if self.head is None:
            return None

        prev_min = None
        min_node = self.head
        prev = None
        current = self.head

        while current:
            if current.priority < min_node.priority:
                min_node = current
                prev_min = prev
            prev = current
            current = current.sibling

        if prev_min is None:
            self.head = min_node.sibling
        else:
            prev_min.sibling = min_node.sibling

        child_queue = PriorityQueue()
        if min_node.child:
            child = min_node.child
            prev_child = None

            while child:
                next_child = child.sibling
                child.sibling = prev_child
                child.parent = None
                prev_child = child
                child = next_child

            child_queue.head = prev_child

        self._merge(child_queue)

        return (min_node.value, min_node.priority)

    def _merge(self, other_queue):
        """Слияние двух биномиальных куч"""
        if other_queue.head is None:
            return

        if self.head is None:
            self.head = other_queue.head
            other_queue.head = None
            return

        im_head = Node(None, None)
        tail = im_head

        h1 = self.head
        h2 = other_queue.head

        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.sibling = h1
                h1 = h1.sibling
            else:
                tail.sibling = h2
                h2 = h2.sibling
            tail = tail.sibling

        if h1:
            tail.sibling = h1
        else:
            tail.sibling = h2

        prev = im_head
        x = im_head.sibling
        next_node = x.sibling if x else None

        while next_node:
            if x.degree != next_node.degree or (
                next_node.sibling and next_node.sibling.degree == x.degree
            ):
                prev = x
                x = next_node
            else:
                if x.priority <= next_node.priority:
                    x.sibling = next_node.sibling
                    next_node.parent = x
                    next_node.sibling = x.child
                    x.child = next_node
                    x.degree += 1
                else:
                    if prev == im_head:
                        im_head.sibling = next_node
                    else:
                        prev.sibling = next_node
                    x.parent = next_node
                    x.sibling = next_node.child
                    next_node.child = x
                    next_node.degree += 1
                    x = next_node

            next_node = x.sibling if x else None

        self.head = im_head.sibling
        other_queue.head = None

    def decrease_key(self, node, new_priority):
        """Уменьшение приоритета элемента"""
        if new_priority > node.priority:
            raise ValueError("Новый приоритет должен быть меньше")

        node.priority = new_priority
        parent = node.parent

        while parent and node.priority < parent.priority:
            node.value, parent.value = parent.value, node.value
            node.priority, parent.priority = parent.priority, node.priority

            node = parent
            parent = node.parent

    def delete(self, node):
        """Удаление элемента"""
        self.decrease_key(node, self.MIN_PRIORITY)
        return self.extract_min()
