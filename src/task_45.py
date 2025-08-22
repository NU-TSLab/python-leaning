class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        print(f"幅:{self.width}、高さ:{self.height}")

kukei=Rectangle(20,10)
print(kukei.area())
kukei.__str__()