"""
Returns a list of all the data in the binary search tree in sorted order.

Returns:
list: A sorted list of all the data in the binary search tree.
"""


class TreeNode:
    """
    A node in a binary search tree.

    Args:
        data: The data stored in the node.
        left: The left child node.
        right: The right child node.

    Methods:
        __str__(): Returns a string representation of the node.
        append(value): Inserts a new value into the binary search tree.
        get_data(): Returns a list of all the data in the binary search tree in sorted order.
    """

    def __init__(self, data, left=None, right=None):
        """
        Initializes a node in a binary search tree.

        Args:
            data: The data stored in the node.
            left: The left child node.
            right: The right child node.
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: A string representation of the node.
        """
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"

    def append(self, value):
        """
        Inserts a new value into the binary search tree.

        Args:
            value: The value to be inserted.
        """
        if int(value) > int(self.data):
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.append(value)
        else:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.append(value)


    def get_data(self):
        """
        Returns a list of all the data in the binary search tree in sorted order.

        Returns:
            list: A sorted list of all the data in the binary search tree.
        """
        data = []
        if self.left is not None:
            data.extend(self.left.get_data())
        data.append(self.data)
        if self.right is not None:
            data.extend(self.right.get_data())
        return data


class BinarySearchTree:
    """
    A binary search tree implementation.

    Args:
        tree_data (list): A list of integers representing the tree data.

    Attributes:
        root (TreeNode): The root node of the binary search tree.

    Methods:
        data(): Returns the root node of the binary search tree.
        sorted_data(): Returns a sorted list of all the data in the binary search tree.
    """

    def __init__(self, tree_data):
        """
        Initializes a binary search tree with the given tree data.

        Args:
            tree_data (list): A list of integers representing the tree data.
        """
        root = tree_data[0]
        rest = tree_data[1:]
        self.root = TreeNode(root)
        for branch in rest:
            self.root.append(branch)

    def data(self):
        """
        Returns the root node of the binary search tree.

        Returns:
            TreeNode: The root node of the binary search tree.
        """
        return self.root

    def sorted_data(self):
        """
        Returns a sorted list of all the data in the binary search tree.

        Returns:
            list: A sorted list of all the data in the binary search tree.
        """
        return self.root.get_data()
