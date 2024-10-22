class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    def car_info(self): 
        return f"{self.make}の車、年式：{self.year}"
    
a=Car("日産",2019)
print(a.car_info())