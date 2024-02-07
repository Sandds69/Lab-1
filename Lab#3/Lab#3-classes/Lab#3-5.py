class Account:
    def __init__(self, owner, balance=400):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if(self.balance < amount):
            return 0
        else:
            self.balance -= amount
            return self.balance