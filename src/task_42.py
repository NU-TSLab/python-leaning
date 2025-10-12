class BankAcount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount

person1 = BankAcount()
person1.deposit(1000)
person1.withdraw(500)
print(person1.balance)
person1.withdraw(600)
print(person1.balance)