class BankAcount:
    def __init__(self):
        self.balance=0


        
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if self.balance<amount:
            print("残高不足")
            return self.balance
        else:
            self.balance-=amount
            return self.balance
        

mybank=BankAcount()

print(f"預け入れ後の残高:{mybank.deposit(10000)}")
print(f"預け入れ後の残高:{mybank.deposit(23000)}")
print(f"引き出し後の残高:{mybank.withdraw(3000)}")
print(f"引き出し後の残高:{mybank.withdraw(40000)}")
