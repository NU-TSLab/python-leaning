class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        
def find_top_student(students):
    return max(students, key=lambda student: student.grade).name
    
students=[Student("Yukie",20),Student("Keshin",30),Student("Mari",40)]
top=find_top_student(students)
print(top)


