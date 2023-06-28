"""Hey BOB
"""

def cleanup(hey_bob):
    text = "".join([c for c in hey_bob if c.isalnum() or c == "?"])
    return text


def is_question(text):
    return text[-1] == "?"


def all_capitals(text):
    return text.isupper()


def is_nothing(text):
    return text == ""


def response(hey_bob):
    text=cleanup(hey_bob)

    if is_nothing(text):
        return "Fine. Be that way!"

    if is_question(text):
        if all_capitals(text):
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."

    if all_capitals(text):
        return "Whoa, chill out!"

    return "Whatever."
