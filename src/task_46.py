class Emloyee:
    def __init__(self):
        self._salary = 0
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給与は0以上で設定してください")
        else:
            self._salary = value

emp = Emloyee()
emp.salary = 5000
print("給与:", emp.salary)
emp.salary = -3000
print("給与:", emp.salary)