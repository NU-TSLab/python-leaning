class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給料が0未満です")
        else:
            self._salary = value

human = Employee()
human.salary = 50000
print(human.salary)

human.salary = -200