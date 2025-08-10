class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def speak(self):
        return "ワンワン"
    
class Cat(Animal):
    def speak(self):
        return "ニャー"    
    
dog = Dog("kira")
cat = Cat("rara")
print(dog.speak())  
print(cat.speak()) 