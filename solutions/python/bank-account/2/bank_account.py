from threading import Lock


class BankAccount:
    def __init__(self):
        self._balance = 0
        self._isopen = False
        self._mutex = Lock()

    def get_balance(self):
        with self._mutex:
            if not self._isopen:
                raise ValueError("account not open")
            return self._balance

    def open(self):
        with self._mutex:
            if self._isopen:
                raise ValueError("account already open")
            self._isopen = True

    def deposit(self, amount):
        with self._mutex:
            if not self._isopen:
                raise ValueError("account not open")
            if amount < 0:
                raise ValueError("amount must be greater than 0")
            self._balance += amount

    def withdraw(self, amount):
        with self._mutex:
            if not self._isopen:
                raise ValueError("account not open")
            if amount < 0:
                raise ValueError("amount must be greater than 0")
            if amount > self._balance:
                raise ValueError("amount must be less than balance")
            self._balance -= amount

    def close(self):
        with self._mutex:
            if not self._isopen:
                raise ValueError("account not open")
            self._isopen = False
            self._balance = 0

