class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"„‚Í{self.name}‚Å‚·A{self.age}Î‚Å‚·"

p = Person("Haru", 22)
print(p.introduce())