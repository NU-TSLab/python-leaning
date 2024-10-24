import csv

class Student:
    def __init__(self,name,score_list):
        self.name = name
        self.score_list = score_list
    
    def get_average_score(self):
        l = len(self.score_list)
        if l != 0:
            return sum(self.score_list) / len(self.score_list)
        return 0
    
    def display_score(self):
        return f"{self.name}の平均点:{self.get_average_score(self.score_list):2}点"

class Grade:
    def __init__(self,student_list,subject_list):
        self.student_list = student_list
        self.subject_list = subject_list
    
    def get_high_score(self):
        highest_student = max(self.student_list, key=lambda x: x.get_average_score())
        return f"最高得点獲得者{highest_student.name}の平均点:{highest_student.get_average_score():2}点"

with open('./data/task_56.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    subject_list = next(reader)[1:] 

    student_list = []
    for row in reader:
        name = row[0]
        scores = [int(score) for score in row[1:]]
        student = Student(name, scores)
        student_list.append(student)


grade = Grade(student_list, subject_list)
print(grade.get_high_score())
