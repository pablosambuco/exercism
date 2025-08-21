class Node:
    def __init__(self, value, next_=None, prev_=None):
        self.value = value
        self.next_ = next_
        self.prev_ = prev_

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        aux = self.head
        while aux:
            yield aux
            aux = aux.next_

    def __len__(self):
        return sum(1 for _ in self)

    def __repr__(self):
        return ", ".join(str(node) for node in self)

    def pop(self):
        if not self.head:
            raise IndexError("List is empty")
        old = self.tail.value
        self.tail = self.tail.prev_
        if self.tail:
            self.tail.next_ = None
        else:
            self.head = None
        return old

    def push(self, number):
        new = Node(number)
        if not self.tail:
            self.head = new
        else:
            new.prev_ = self.tail
            self.tail.next_ = new

        self.tail = new

    def shift(self):
        if not self.head:
            raise IndexError("List is empty")
        old = self.head.value
        self.head = self.head.next_

        if self.head:
            self.head.prev_ = None
        else:
            self.tail = None
        return old

    def unshift(self, number):
        aux = Node(number, next_=self.head)
        if self.head:
            self.head.prev_ = aux
        self.head = aux

    def delete(self, value):
        for aux in self:
            if aux.value == value:
                if aux.prev_:
                    aux.prev_.next_ = aux.next_
                if aux.next_:
                    aux.next_.prev_ = aux.prev_
                if aux == self.head:
                    self.head = aux.next_
                if aux == self.tail:
                    self.tail = aux.prev_
                break
        else:
            raise ValueError("Value not found")
