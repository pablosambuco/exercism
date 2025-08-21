class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = self.tail = 0
        self.is_empty = True
        self.is_full = False

    def read(self):
        if self.is_empty:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail += 1
        if self.tail == self.capacity:
            self.tail -= self.capacity
        if self.tail == self.head:
            self.is_empty = True
        self.is_full = False
        return data

    def write(self, data):
        if self.is_full:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.head] = data
        self.head += 1
        if self.head == self.capacity:
            self.head -= self.capacity
        if self.head == self.tail:
            self.is_full = True
        self.is_empty = False

    def overwrite(self, data):
        if self.is_full:
            self.buffer[self.tail] = data
            self.tail += 1
            if self.tail == self.capacity:
                self.tail -= self.capacity
        else:
            self.buffer[self.head] = data
        self.head += 1
        if self.head == self.capacity:
            self.head -= self.capacity
        if self.head == self.tail:
            self.is_full = True
        self.is_empty = False

    def clear(self):
        if not self.is_empty:
            self.buffer[self.tail] = None
            self.tail += 1
            if self.tail == self.capacity:
                self.tail -= self.capacity
            if self.tail == self.head:
                self.is_empty = True
            self.is_full = False
