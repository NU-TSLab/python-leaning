class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"(矩形 幅:{self.width},  高さ:{self.height})"
    
rect = Rectangle(10, 20)
print(rect)
print(rect.get_area())

#(矩形 幅:10,  高さ:20)
#200