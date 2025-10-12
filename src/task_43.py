class Animal:
    def __init__(self, nmae):
        self.name = nmae
    
class Dog(Animal):
    def speak(self):
        print("ワンワン")

class Cat(Animal):
    def speak(self):
        print("ニャーニャー")

dog = Dog("ポチ")
cat = Cat("タマ")

dog.speak()
cat.speak()