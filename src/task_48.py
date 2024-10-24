class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, money):
        if money < 0:
            print("エラーです")
        else:
            self._salary = money


result = Employee()
result.salary = 10000
print(result.salary)
result.salary = -7000
