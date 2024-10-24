class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def car_info(self):
        return f"{self.make}‚ÌÔA”N®:{self.year}"

car = Car("Mustang", 1968)
print(car.car_info())