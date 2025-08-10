class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        return f"私は{self.name}です。{self.age}歳です。"

p=Person("太郎",20)
print(p.introduce())