class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height
    
    def area(self):
        return print(self.width * self.height)
    
    def __str__(self):
        return print("幅:" ,self.width , "高さ:" , self.height)
    
Rectangle(4 , 5).area()
Rectangle(4 , 5).__str__()