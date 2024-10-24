import csv
student_list=[]
#subject_list = ['国語', '数学', '英語', '理科', '社会', '音楽', '美術', '体育']

class Student:
    def __init__(self,name,score_list):
        self.name=name
        self.score_list=score_list

    def get_average_score(self):
        return sum(self.score_list)/len(self.score_list)
    
    def display_score(self):
        print (f"生徒の名前：{self.name},平均点：{self.get_average_score()}")


class Grade:
    def __init__(self,student_list,subject_list):
        self.student_list = student_list
        self.subject_list = subject_list

    def get_high_score(self):
        top_student=max(self.student_list,key=lambda s:s.get_average_score())
        print (f"最高得点者：{top_student.name}、平均点：{top_student.get_average_score()}")

subject_list=[]
with open("./data/task_56.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    next(reader)#1行目intだめとばす
    for row in reader:
        name=row[0]#1列目は名前
        scores=list(map(int,row[1:]))#２列目以降の得点
        student_list.append(Student(name,scores))
grade = Grade(student_list, subject_list)
grade.get_high_score()

