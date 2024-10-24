class Rectangle:

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        s=self.width* self.height
        return s
    
    def __str__(self):
        return f"幅：{self.width}  高さ:{self.height} "
    
Rectangle1=Rectangle(3,4)

print(Rectangle1)
print(Rectangle1.area())

