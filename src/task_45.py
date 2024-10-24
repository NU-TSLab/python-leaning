class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def nakigoe(self):
        return "ワンワン"


class Cat(Animal):
    def nakigoe(self):
        return "ニャー"


dog = Dog("柴犬")
cat = Cat("キティ")
print(dog.nakigoe())
print(cat.nakigoe())
