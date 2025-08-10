class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

def find_top_student(students):
        return max(students, key=lambda student: student.grade).name

students = [
    Student("すずな", 85),
    Student("たろう", 90),
    Student("はなこ", 95)
]
top_student = find_top_student(students)
print(top_student)