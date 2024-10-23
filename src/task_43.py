class Animal:
    def __init__(self , name):
        self.name = name
    
class Dog(Animal):
    def speak(self):
        return print("ワンワン!!!")

class Cat(Animal):
    def speak(self):
        return print("ニャー!")

Dog("犬公").speak()
Cat("ネコマン").speak()