class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposite(self, amount):
         self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("c‚•s‘«")
        else:
            self.balance -= amount