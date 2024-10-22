class Rectangle:
    def __init__(self,width,hight):
        self.width=width
        self.hight=hight

    def area(self):
        mennseki=self.width*self.hight
        return mennseki
    
    def __str__(self):
        return f"幅は{self.width}で高さは{self.hight}です。"
a=Rectangle(3,4)
print(a)
print(a.area())