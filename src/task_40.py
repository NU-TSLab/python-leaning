class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"����{self.name}�ł��A{self.age}�΂ł�"

p = Person("Haru", 22)
print(p.introduce())