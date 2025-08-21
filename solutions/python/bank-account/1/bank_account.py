class BankAccount:
    def __init__(self):
        self.balance=0
        self.isopen=False

    def get_balance(self):
        if not self.isopen:
            raise ValueError('account not open')        
        return self.balance

    def open(self):
        if self.isopen:
            raise ValueError('account already open')        
        self.isopen = True

    def deposit(self, amount):
        if not self.isopen:
            raise ValueError('account not open')
        if amount < 0:
            raise ValueError('amount must be greater than 0')
        self.balance += amount

    def withdraw(self, amount):
        if not self.isopen:
            raise ValueError('account not open')
        if amount < 0:
            raise ValueError('amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')        
        self.balance -= amount

    def close(self):
        if not self.isopen:
            raise ValueError('account not open')        
        self.isopen = False
        self.balance = 0
