class InputCell:
    """A cell that holds a value and notifies dependents on change."""
    def __init__(self, value):
        self._value = value
        self.callbacks = []
        self.dependents = set()

    @property
    def value(self):
        """Get the current value"""
        return self._value

    def set_value(self, value):
        """Set the value without propagation"""
        self._value = value

    @value.setter
    def value(self, value):
        """Set the value and propagate changes"""
        if self._value != value:
            self._value = value

            affected = []
            queue = list(self.dependents)
            for cell in queue:
                if cell not in affected:
                    affected.append(cell)
                    if hasattr(cell, "dependents"):
                        queue.extend(cell.dependents)

            ordered = []
            visited = set()

            def visit(cell):
                if cell in visited:
                    return
                visited.add(cell)
                if hasattr(cell, "inputs"):
                    for inp in cell.inputs:
                        if inp in affected:
                            visit(inp)
                ordered.append(cell)

            for cell in affected:
                visit(cell)

            changed = set()
            for cell in ordered:
                if hasattr(cell, "compute_function"):
                    old = cell.value
                    new = cell.compute_function(cell.inputs)
                    if old != new:
                        cell.set_value(new)
                        changed.add(cell)

            for cell in changed:
                for cb in cell.callbacks:
                    cb(cell.value)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return f"({self._value},{len(self.callbacks)})"

    def __add__(self, other):
        return self._value + other

    def __radd__(self, other):
        return self._value + other

    def __sub__(self, other):
        return self._value - other

    def __rsub__(self, other):
        return other - self._value

    def __mul__(self, other):
        return self._value * other

    def __rmul__(self, other):
        return self._value * other

    def __lt__(self, other):
        return self._value < other

    def __eq__(self, other):
        return self._value == other

    def add_callback(self, callback):
        """adds a callback object to the list"""
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        """removes a callback object from the list"""
        if callback in self.callbacks:
            self.callbacks.remove(callback)


class ComputeCell(InputCell):
    """A cell whose value is computed from other cells."""    
    def __init__(self, inputs, compute_function):
        self.compute_function = compute_function
        self.inputs = inputs
        super().__init__(compute_function(inputs))
        for i in inputs:
            if hasattr(i,'dependents'):
                i.dependents.add(self)
