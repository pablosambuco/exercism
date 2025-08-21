def is_armstrong_number(number):
    number_text = str(number)
    power = len(number_text)
    armstrong = sum(int(c)**power for c in number_text)
    return number==armstrong
