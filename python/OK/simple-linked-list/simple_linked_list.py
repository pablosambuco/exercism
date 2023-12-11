class Node:
    def __init__(self, value, succeding=None):
        self.node_value = value
        self.succeding = succeding

    def value(self):
        return self.node_value

    def next(self):
        return self.succeding

    def __repr__(self):
        return str(self.node_value)


class LinkedList:
    def __init__(self, values=[]):
        self.header = None
        self.tail = None
        for value in values:
            self.push(value)
        self.current = None

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        aux = self.header
        self.current = self.header
        while aux:
            yield aux.value()
            aux = aux.next()

    def __repr__(self):
        return "[" + ", ".join(str(node) for node in self) + "]"

    def head(self):
        if not self.header:
            raise EmptyListException("The list is empty.")
        return self.header

    def push(self, value):
        aux = Node(value, self.header)
        self.header = aux

    def pop(self):
        if not self.header:
            raise EmptyListException("The list is empty.")
        aux = self.header
        self.header = self.header.next()
        return aux.value()

    def reversed(self):
        content = []
        aux = self.header
        while aux:
            content.append(aux.value())
            aux = aux.next()
        return reversed(content)


class EmptyListException(Exception):
    pass
