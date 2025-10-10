class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "ワンワン"
    
class Cat(Animal):
    def speak(self):
        return "ニャー"
    
d = Dog("大五郎")
print(d.speak())

c = Cat("紋次郎")
print(c.speak() + c.speak())