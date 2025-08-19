class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"残高:{self.balance}円")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"残高:{self.balance}円")
        else:
            print("残高不足です。")

p = BankAccount()
p.deposit(2000)
p.withdraw(3000)
p.withdraw(1500)
