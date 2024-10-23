class BankAccount:
    def __init__(self , balance = 0):
        self.balance = balance

    def deposit(self , amount):
        self.balance = amount + self.balance
        return print(self.balance)

    def withdraw(self , amount):
        if(amount > self.balance):
            return print("残高不足")
        else:
            self.balance = self.balance - amount
            return print(self.balance)

n = BankAccount()
n.deposit(1000)
n.deposit(300)
n.withdraw(600)
n.withdraw(700)
n.withdraw(100)