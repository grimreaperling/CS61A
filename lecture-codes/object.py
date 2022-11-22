class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name 

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return 
        self.balance -= amount
        return self.balance




