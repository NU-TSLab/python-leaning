class Employee:
    def __init__(self , _salary = 0):
        self._salary = _salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self , n):
        if(n<0):
            return print("エラー")
        else:
            self._salary = n

m = Employee()
m.salary = 300000
print(m.salary)
m.salary = -100000

        
    
