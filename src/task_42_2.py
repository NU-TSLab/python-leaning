class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

def find_top_student(students):
    return max(students,key=lambda student: student.grade).name

students=[Student("太郎",50),Student("次郎",89),Student("三郎",47)]
top_student=find_top_student(students)
print(top_student)