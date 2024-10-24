class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        return f"私は{self.name}です。{self.age}歳です。"
    
jibun=Person("yume",21)

print(jibun.introduce())

"""
クラスのメソッドの第一引数はself
メソッドとしてintroduce

"""