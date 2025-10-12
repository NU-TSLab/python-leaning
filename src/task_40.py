class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"私は{self.name}です。{self.age}歳です。")
        
person1 = Person("太郎", 30)
person1.introduce()