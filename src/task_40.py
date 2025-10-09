# task_40.py
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"私は{self.name}です．{self.age}歳です．"
    
person = Person("shion",21)
print(person.introduce())
