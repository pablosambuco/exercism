class CustomSet:
    def __init__(self, elements=[]):
        self.elements = []
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    def isempty(self):
        return not self.elements

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.isempty() or all(
            element in other.elements for element in self.elements
        )

    def isdisjoint(self, other):
        return all(element not in self.elements for element in other.elements)

    def __eq__(self, other):
        return len(self) == len(other) and self.issubset(other)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def intersection(self, other):
        return CustomSet([element for element in other.elements if element in self.elements])

    def __sub__(self, other):
        aux = CustomSet(self.elements)
        for element in other.elements:
            aux.remove(element)
        return aux

    def __add__(self, other):
        aux = CustomSet(self.elements)
        for element in other.elements:
            aux.add(element)
        return aux

    def __len__(self):
        return len(self.elements)
