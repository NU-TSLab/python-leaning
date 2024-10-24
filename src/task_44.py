class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "ƒƒ“ƒƒ“"

class Cat(Animal):
    def speak(self):
        return "ƒjƒƒ["

dog = Dog("Kuro")
cat = Cat("Shiro")
print(dog.speak())
print(cat.speak())