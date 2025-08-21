def proverb(*input_data, qualifier=None):
    if not input_data:
        return []

    if qualifier:
        qualifier = qualifier + " "
    else:
        qualifier = ""

    output = []

    and_all, *for_a_want = input_data
    pword = and_all
    for word in for_a_want:
        output.append(f"For want of a {pword} the {word} was lost.")
        pword = word
    output.append(f"And all for the want of a {qualifier}{and_all}.")

    return output
