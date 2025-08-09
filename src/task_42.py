class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance +=amount
    
    def withdraw(self,amount):
        if self.balance < amount:
            print("残高不足")
        else:
            self.balance-=amount

bank=BankAccount()
bank.deposit(1000)
bank.withdraw(600)
bank.withdraw(700)