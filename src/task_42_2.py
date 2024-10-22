class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def find_top_student(students): 
    top_student = students[0]  
    for student in students:
        if student.grade > top_student.grade:
            top_student = student
    return top_student.name

students = [Student("佐野", 85),Student("田中", 92),Student("勝本", 77),Student("栗田", 88)]
top_student_name = find_top_student(students)
print(f"成績が最も高い学生は {top_student_name} です。")


