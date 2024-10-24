class Animal:

    def __init__(self,name):
        self.name=name

class Dog(Animal):
    
    def speak(self):
        nakigoe="ワンワン"
        return nakigoe
    
class Cat(Animal):
    def speak(self):
        nakigoe="ニャー"
        return nakigoe

mydog=Dog("pochi")
mycat=Cat("tama")
print(f"{mydog.name}は{mydog.speak()},{mycat.name}は{mycat.speak()}")
    
