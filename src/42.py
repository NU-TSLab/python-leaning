class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount

account = BankAccount()
account.deposit(80000)
account.withdraw(35672)
account.withdraw(25476)