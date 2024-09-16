class PhoneNumber:
    def __init__(self, number):
        self.area_code, self.exchange_code, self.suscriber = self.cleanup(number)

    @property
    def number(self):
        return self.area_code + self.exchange_code + self.suscriber

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.suscriber}"

    def cleanup(self, number: str):
        # Remove valid punctuation
        number = number.translate({ord(i): None for i in "+()-. "})

        # Are ther any invalid characters?
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")

        if not all(c.isdigit() for c in number):
            raise ValueError("punctuations not permitted")

        # Count digits
        digits = len(number)
        if digits < 10:
            raise ValueError("must not be fewer than 10 digits")
        if digits > 11:
            raise ValueError("must not be greater than 11 digits")

        # Validate 11 digits number
        if digits == 11:
            if not number.startswith("1"):
                raise ValueError("11 digits must start with 1")
            number = number[1:]

        area_code = number[0:3]
        exchange_code = number[3:6]
        number = number[6:]

        if area_code.startswith("0"):
            raise ValueError("area code cannot start with zero")
        if area_code.startswith("1"):
            raise ValueError("area code cannot start with one")
        if exchange_code.startswith("0"):
            raise ValueError("exchange code cannot start with zero")
        if exchange_code.startswith("1"):
            raise ValueError("exchange code cannot start with one")

        return area_code, exchange_code, number
