import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._r_bytes = 0
        self._w_bytes = 0
        self._r_ops = 0
        self._w_ops = 0
        self._open = False

    def __enter__(self):
        self._open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._open = False
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        data = super().readline()
        self._r_bytes += len(data)
        self._r_ops += 1
        if not data:
            raise StopIteration
        return data

    def read(self, size=-1):
        data = super().read(size)
        self._r_bytes += len(data)
        self._r_ops += 1
        return data

    @property
    def read_bytes(self):
        return self._r_bytes

    @property
    def read_ops(self):
        return self._r_ops

    def write(self, data):
        len_data = super().write(data)
        self._w_bytes += len_data
        self._w_ops += 1
        return len_data

    @property
    def write_bytes(self):
        return self._w_bytes

    @property
    def write_ops(self):
        return self._w_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._r_bytes = 0
        self._s_bytes = 0
        self._r_ops = 0
        self._s_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self._r_bytes += len(data)
        self._r_ops += 1
        return data

    @property
    def recv_bytes(self):
        return self._r_bytes

    @property
    def recv_ops(self):
        return self._r_ops

    def send(self, data, flags=0):
        len_data = self._socket.send(data, flags)
        self._s_bytes += len_data
        self._s_ops += 1
        return len_data

    @property
    def send_bytes(self):
        return self._s_bytes

    @property
    def send_ops(self):
        return self._s_ops
