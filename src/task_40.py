class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def introduct(self):
        return print("私は",self.name,"です。",self.age,"歳です。")
Person("幕田",20).introduct()
Person("亮介",20).introduct()