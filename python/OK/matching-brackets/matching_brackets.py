def is_paired(input_string):
    pairs = {"}": "{", "]": "[", ")": "("}
    stack = []

    for char in input_string:
        if char in pairs.values():
            stack.append(char)
        if char in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return not stack
