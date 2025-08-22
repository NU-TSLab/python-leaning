class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def speak(self):
        print("ワンワン")

class Cat(Animal):
    def speak(self):
        print("ニャー")
    
dog=Dog("Shiro")
cat=Cat("Nyarosuke")
dog.speak()
cat.speak()
