import re


class Luhn:

    map = {digit: digit * 2 - (9 if digit >= 5 else 0) for digit in range(10)}

    def __init__(self, card_num):
        self.card_num = card_num
        self.clean_value = re.sub("[^0-9]", "", card_num)

    def value(self):
        value = 0
        for index, digit in enumerate(reversed(self.clean_value)):
            digit = int(digit)
            if index % 2 == 1:
                digit = Luhn.map[digit]
            value += digit
        return value

    def valid(self):

        if re.search("[^0-9 ]", self.card_num):
            return False

        if self.clean_value == "0":
            return False

        return self.value() % 10 == 0
