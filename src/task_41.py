class Car:
    def __init__(self , make , year):
        self.make = make
        self.year = year
    
    def car_info(self):
        return print(self.make , "の車、年式:",self.year)

Car("ふぉるくすわーげん" , 2010).car_info()