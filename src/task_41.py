class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"私は{self.name}です。{self.age}歳です。"


human = Person("慎一郎", 21)
print(human.introduce())
