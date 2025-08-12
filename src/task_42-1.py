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
print(account.balance)
account.deposit(1000)
print(account.balance)
account.withdraw(300)
print(account.balance)
account.withdraw(10000)
print(account.balance)