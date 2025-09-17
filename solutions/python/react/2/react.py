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

    @value.setter
    def value(self, value):
        if self._value != value:
            self._value = value
            changed = {}
            for dep in self.dependents:
                dep.recompute(changed)
            for cell, original_value in changed.items():
                if cell.value != original_value:
                    for cb in cell.callbacks:
                        cb(cell.value)


class ComputeCell(InputCell):
    """A cell whose value is computed from other cells."""

    def __init__(self, inputs, compute_function):
        super().__init__(compute_function([i.value for i in inputs]))
        self.inputs = inputs
        self.compute_function = compute_function
        for i in inputs:
            i.dependents.add(self)

    def recompute(self, changed={}):
        new = self.compute_function([i.value for i in self.inputs])
        if new != self._value:
            changed.setdefault(self, self._value)
            self._value = new
            for dep in self.dependents:
                dep.recompute(changed)

    def add_callback(self, callback):
        """adds a callback object to the list"""
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        """removes a callback object from the list"""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
