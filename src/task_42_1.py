class BankAcount:
    def __init__(self):
        self.balance=0
    
    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("残高不足")
        else:
            self.balance=self.balance-amount

a=BankAcount()
a.deposit(5000)
a.withdraw(2000)
a.withdraw(4000)