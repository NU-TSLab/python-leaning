class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount

bank = BankAccount()
bank.deposit(1000000)
bank.withdraw(2000000)
bank.withdraw(999999)
        

