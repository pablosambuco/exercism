def aliquot(number):
    div=[]
    for i in range(1,number//2+1):
        if number % i == 0:
            div.append(i)
    return sum(div)

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int):
        raise TypeError("Classification is only possible for positive integers.")
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    ali = aliquot(number)
    if number == ali:
        return "perfect"
    if number < ali:
        return "abundant"
    return "deficient"

