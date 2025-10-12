import csv

class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list
    
    def get_average_score(self):
        return sum(self.score_list) / len(self.score_list)
    
    def display_info(self):
        average = self.get_average_score()
        print(f"{self.name}さんの平均点は{average:.2f}点です。")
    
class Grade:
    def __init__(self, sunject_list):
        self.student_list = []
        self.subject_list = sunject_list
    #student_listにStudentオブジェクトを追加
    def add_student(self, student):
        self.student_list.append(student)
    
    def get_high_score(self):
        #student_listからget_average_score()が最も高いStudentオブジェクトを取得
        highest_avg_student = max(self.student_list, key=lambda student: student.get_average_score())
        highest_avg = highest_avg_student.get_average_score()
        print(f"最高平均点は{highest_avg_student.name}さんの{highest_avg:.2f}点です。")

subject_list = []
grade=None
with open("./data/task_56.csv",newline="", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):    #enumrate関数：リストの要素とそのインデックスを同時に取得
        print(i," ",row)
        if i == 0:
            subject_list = row[1:]
            grade = Grade(subject_list)
        else:
            name = row[0]
            scores = list(map(int, row[1:]))    #map関数：リストの各要素に対して関数を適用
            student = Student(name, scores)
            grade.add_student(student)

grade.get_high_score()