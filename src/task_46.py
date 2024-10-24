class Employee:
    def __init__(self,salary):
        self._salary=salary

    @property
    def salary(self):
        return  self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("給与は0以上にしてください")
        else:
            self._salary = value
    #クラス内は_salaryで統一

emp = Employee(0)  
print(f"初期 salary: {emp.salary}") #これでゲッター呼び出し

emp.salary = 60000 #代入文でセッター呼び出し
print(f"変更後 salary: {emp.salary}")

emp.salary = -100 
print(f"変更後 salary: {emp.salary}")