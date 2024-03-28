def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if any(preorder.count(item) > 1 for item in preorder) or any(
        inorder.count(item) > 1 for item in inorder
    ):
        raise ValueError("traversals must contain unique items")

    if any(item not in inorder for item in preorder) or any(
        item not in preorder for item in inorder
    ):
        raise ValueError("traversals must have the same elements")

    if not (preorder):
        return {}

    root = preorder[0]
    pos = inorder.index(root)
    inorder_left = inorder[:pos]
    inorder_right = inorder[pos + 1 :]
    preorder_left = preorder[1 : 1 + len(inorder_left)]
    preoder_right = preorder[1 + len(inorder_left) :]

    return {
        "v": root,
        "l": tree_from_traversals(preorder_left, inorder_left),
        "r": tree_from_traversals(preoder_right, inorder_right),
    }
