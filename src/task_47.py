class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def __str__(self):
        return f"矩形幅{self.width}、高さ{self.height}"


result = Rectangle(5, 10)
print(result)
print(result.area())
