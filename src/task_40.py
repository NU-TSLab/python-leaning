class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"私は{self.name}です。年齢は{self.age}です。"
p=Person("Yuuki",20)
print(p.introduce())