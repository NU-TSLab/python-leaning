class BankAccount:
    def __init__ (self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw (self, amount):
        if amount > self.balance:
            print("残高不足")
        else :
            self.balance -= amount

acounnt = BankAccount()
acounnt.deposit(10000)
acounnt.withdraw(5000)
acounnt.withdraw(10000)