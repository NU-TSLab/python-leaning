class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if self.balance < amount:
            print("残高不足")
            return f"あと{amount-self.balance}円足りません。"
        else:
            self.balance -= amount
            return self.balance

bank=BankAccount()

print(bank.deposit(20000))

print(bank.withdraw(1000))

print(bank.withdraw(20000))
