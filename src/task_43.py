class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def speak(self):
        return "ワンワン"
    
class Cat(Animal):
    def speak(self):
        return "ニャー"
    
dog=Dog("ポチ")
cat=Cat("タマ")
print(dog.speak())
print(cat.speak())