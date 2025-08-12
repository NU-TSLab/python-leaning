class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def speak(self):
        return"わんわん"
class cat(animal):
    def speak(self):
        return"ニャー"
dog=dog("pochi")
cat=cat("tama")
print(dog.speak())
print(cat.speak())