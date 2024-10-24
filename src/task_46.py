class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"‹éŒ` •: {self.width}, ‚‚³: {self.height}"

rect = Rectangle(328, 101)
print(rect)
print(rect.area())