class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
       
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on a balance")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive")

acc = Account("Air", 12000)
acc.deposit(9300)
acc.withdraw(4400)