from json import dumps

class Tree:
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def add_child(self, other):
        self.children.append(other)

    def remove_child(self, label):
        for child in self.children:
            if child.label == label:
                self.children.remove(child)

    def from_pov(self, from_node, is_root = True):
        if from_node == self.label:
            return self
        for child in self.children:
            if child.label == from_node:
                self.remove_child(child.label)
                return Tree(child.label, child.children + [self])
            new_self = child.from_pov(from_node, False)
            if child.label != new_self.label:
                self.remove_child(child.label)
                child.add_child(self)
                return new_self
        if is_root:
            raise ValueError("Tree could not be reoriented")
        return self

    def path_to_child(self, to_node):
        current_path = [self.label]
        if to_node == self.label:
            return current_path

        for child in self.children:
            child_path = child.path_to_child(to_node)
            if child_path:
                current_path.extend(child_path)
                return current_path
        return []

    def path_to(self, from_node, to_node):
        tree = self.from_pov(from_node)
        path = tree.path_to_child(to_node)
        if not path:
            raise ValueError("No path found")
        return path
