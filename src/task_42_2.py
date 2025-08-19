class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students):
    return max(students, key=lambda student: student.grade).name
    
students = [Student("Takuma", 85), Student("Suetake", 90), Student("tatutake", 30)]
print(find_top_student(students))