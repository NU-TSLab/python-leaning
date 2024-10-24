import csv

class Student:
    def __init__(self, name, scores_list):
        self.name = name
        self.scores_list = scores_list

    def get_average_score(self):
        return sum(self.scores_list) / len(self.scores_list)
    
    def display_score(self):
        average = self.get_average_score()
        print(f"{self.name}の平均点: {average:.2f}")
    

class Grade:
    def __init__(self, subject_list):
        self.student_list = []
        self.subject_list = subject_list

    def add_student(self, student):
        self.student_list.append(student)

    def get_high_score(self):
        highest_avg_student = max(self.student_list, key=lambda student: student.get_average_score())
        highest_avg = highest_avg_student.get_average_score()
        print(f"最高平均点の学生: {highest_avg_student.name}, 平均点: {highest_avg:.2f}")

subject_list = []
grade  = None
with open("./data/task_56.csv", "r") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            subject_list = row[1:]
            grade = Grade(subject_list)
        else:
            name = row[0]
            scores = list(map(int, row[1:]))
            student = Student(name, scores)
            grade.add_student(student)

grade.get_high_score()