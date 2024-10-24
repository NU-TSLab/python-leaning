class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "��������"

class Cat(Animal):
    def speak(self):
        return "�j���["

dog = Dog("Kuro")
cat = Cat("Shiro")
print(dog.speak())
print(cat.speak())