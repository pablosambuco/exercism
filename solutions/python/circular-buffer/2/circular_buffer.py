class BufferFullException(BufferError):
    def __init__(self):
        super().__init__("Circular buffer is full")


class BufferEmptyException(BufferError):
    def __init__(self):
        super().__init__("Circular buffer is empty")


class CircularBuffer:
    """A circular buffer implementation with error handling.

    Args:
        capacity (int): The capacity of the circular buffer.
    """

    def __init__(self, capacity):
        """Initialize the CircularBuffer.

        Args:
            capacity (int): The capacity of the circular buffer.
        """
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = self.tail = 0
        self.is_empty = True
        self.is_full = False

    def move_head(self, step=1):
        """Move the head pointer in the circular buffer.

        Args:
            step (int): The number of positions to move the head pointer.
        """
        self.head = (self.head + step) % self.capacity

    def move_tail(self, step=1):
        """Move the tail pointer in the circular buffer.

        Args:
            step (int): The number of positions to move the tail pointer.
        """
        self.tail = (self.tail + step) % self.capacity

    def update_full_status(self):
        """Update the 'is_full' status based on the head and tail pointers."""
        if self.head == self.tail:
            self.is_full = True
        self.is_empty = False

    def update_empty_status(self):
        """Update the 'is_empty' status based on the head and tail pointers."""
        if self.tail == self.head:
            self.is_empty = True
        self.is_full = False

    def read(self):
        """Read data from the circular buffer.

        Returns:
            Any: The data read from the circular buffer.

        Raises:
            BufferEmptyException: If the buffer is empty.
        """
        if self.is_empty:
            raise BufferEmptyException()
        data = self.buffer[self.tail]
        self.move_tail()
        self.update_empty_status()
        return data

    def write(self, data):
        """Write data to the circular buffer.

        Args:
            data (Any): The data to be written to the circular buffer.

        Raises:
            BufferFullException: If the buffer is full.
        """
        if self.is_full:
            raise BufferFullException()
        self.buffer[self.head] = data
        self.move_head()
        self.update_full_status()

    def overwrite(self, data):
        """Write data to the circular buffer, overwriting if it's full.

        Args:
            data (Any): The data to be written to the circular buffer.
        """
        if self.is_full:
            self.buffer[self.tail] = data
            self.move_tail()
        else:
            self.buffer[self.head] = data
        self.move_head()
        self.update_full_status()

    def clear(self):
        """Cleans one position in the circular buffer."""
        if not self.is_empty:
            self.move_tail()
            self.update_empty_status()
