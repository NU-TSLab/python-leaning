class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"私は{self.name}で、年齢は{self.age}歳です。"

P = Person("林 豪杰", 22)
print(P.introduce())

'''
私は林 豪杰で、年齢は22歳です。
'''