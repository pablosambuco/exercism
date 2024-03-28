class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def _sum(x, y):
    return x + y


def _dif(x, y):
    return x - y


def _pro(x, y):
    return x * y


def _div(x, y):
    if not y:
        raise ZeroDivisionError("divide by zero")
    return x // y


func = {
    "+": _sum,
    "*": _pro,
    "-": _dif,
    "/": _div,
}


def evaluate(input_data):
    defs = {}
    stack = []
    for data in input_data:
        words = data.split(" ")
        words.reverse()
        while words:
            print(stack, words)
            word = words.pop().lower()
            print(word)
            # Numbers
            if word.lstrip("-").isnumeric():
                print("Numeric")
                stack.append(int(word))
            # Definitions
            elif word == ":":
                item = words.pop().lower()
                if item.lstrip("-").isnumeric():
                    raise ValueError("illegal operation")
                aux = words.pop().lower()
                value = []
                while aux != ";":
                    if aux in defs:
                        for x in defs[aux]:
                            value.insert(0, x)
                    else:
                        value.insert(0, aux)
                    aux = words.pop().lower()
                defs[item] = value
                print(defs)
            # Using pre-defined words (here, because they can redefine Arithmetics and Stack Operations)
            elif word in defs:
                words.extend(defs[word])
            # Arithmetics
            elif word in ("+", "-", "*", "/"):
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(func[word](op1, op2))
            # Stack Operations
            elif word in ("dup", "swap", "drop", "over"):
                if word == "dup":
                    if not stack:
                        raise StackUnderflowError(
                            "Insufficient number of items in stack"
                        )
                    stack.append(stack[-1])
                elif word == "swap":
                    if len(stack) < 2:
                        raise StackUnderflowError(
                            "Insufficient number of items in stack"
                        )
                    last = stack.pop()
                    stack.insert(-1, last)
                elif word == "drop":
                    if not stack:
                        raise StackUnderflowError(
                            "Insufficient number of items in stack"
                        )
                    stack.pop()
                elif word == "over":
                    if len(stack) < 2:
                        raise StackUnderflowError(
                            "Insufficient number of items in stack"
                        )
                    prev = stack[-2]
                    stack.append(prev)
            # Anythin else
            else:
                raise ValueError("undefined operation")
    return stack
