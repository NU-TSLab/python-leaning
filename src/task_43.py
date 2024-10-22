class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "ワンワン"
    
class Cat(Animal):
    def speak(self):
        return "ニャー"
    
dog=Dog("太郎")
cat=Cat("ミケ")
print(dog.speak())
print(cat.speak())