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


momey = BankAccount()
momey.deposit(70000)
momey.withdraw(100000)
