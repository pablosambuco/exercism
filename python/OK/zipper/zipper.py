class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Zipper:
    def __init__(self, tree, parent=None):
        def iterate(node):
            value = node["value"]
            left = None if node["left"] is None else iterate(node["left"])
            right = None if node["right"] is None else iterate(node["right"])
            return Node(value, left, right)

        self.root = iterate(tree)
        self.parent = parent or []

    @staticmethod
    def from_tree(tree):
        if tree:
            return Zipper(tree)
        return None

    def value(self):
        return self.root.value

    def set_value(self, value):
        self.root.value = value
        return self

    def left(self):
        if self.root.left:
            self.parent += [self.root]
            self.root = self.root.left
            return self

    def set_left(self, tree):
        aux = Zipper.from_tree(tree)
        self.root.left = aux.root if aux else None
        return self

    def right(self):
        if self.root.right:
            self.parent += [self.root]
            self.root = self.root.right
            return self

    def set_right(self, tree):
        aux = Zipper.from_tree(tree)
        self.root.right = aux.root if aux else None
        return self

    def up(self):
        if self.parent:
            self.root = self.parent[-1]
            self.parent = self.parent[:-1]
            return self

    def to_tree(self):
        def to_tree(node):
            if node:
                root = {
                    "value": node.value,
                    "left": to_tree(node.left),
                    "right": to_tree(node.right),
                }
                return root

        root = self.parent[0] if self.parent else self.root
        return to_tree(root)
