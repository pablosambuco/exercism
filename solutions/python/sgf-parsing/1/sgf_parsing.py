class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if "(" not in input_string:
        raise ValueError("tree missing")
    if ";" not in input_string:
        raise ValueError("tree with no nodes")

    root = rec_parse(list(input_string[::-1]))

    return root[0] if root else []


INSTRUCTION_CHARS = ["(", ")", ";", "[", "]"]
NON_ESCAPED_CHARS = ["(", ")", ";", "["]


def rec_parse(input_list):
    node = None
    reading_key = False
    reading_value = False
    key = ""
    prev_key = ""
    value = ""
    values = []
    nodes = []
    is_escaped = False

    while input_list:
        char = input_list.pop()

        if char == "\\":
            is_escaped = True
            char = input_list.pop()
        else:
            is_escaped = False

        if char == "\t":
            char = " "

        if char == "\n" and is_escaped:
            is_escaped = False
            char = ""

        if char in INSTRUCTION_CHARS and not is_escaped:
            if reading_value and value and char in NON_ESCAPED_CHARS:
                value += char
            elif char == ";":
                if node:
                    input_list.append(char)
                    node.children = rec_parse(input_list)
                    input_list = []
                else:
                    node = SgfTree()
                    reading_key = True
            elif char == "[":
                reading_value = True
                reading_key = False
            elif char == "]":
                reading_key = True

                if not key:
                    key = prev_key
                else:
                    values = []

                prev_key = key
                values.append(value)

                node.properties[key] = values
                if prev_key != key:
                    values = []

                value = ""
                key = ""
            elif char == "(":
                if reading_key:
                    input_list.append(char)
                    node.children = rec_parse(input_list[1:])
                    input_list = input_list[:1]
            elif char == ")":
                nodes.append(node)

                node = None
                reading_key = False
                reading_value = False
                key = ""
                prev_key = ""
                value = ""
                values = []
        elif reading_key:
            if "[" not in input_list:
                raise ValueError("properties without delimiter")
            if char != char.upper():
                raise ValueError("property must be in uppercase")
            key += char
        elif reading_value:
            value += char
        else:
            if not key:
                key = prev_key
            node.properties[key] = values
            key = ""
            value = ""
            values = []
            reading_key = True

    if node and not nodes:
        nodes.append(node)
    return nodes
