import csv

class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list

    def get_average_score(self):
        return sum(self.score_list) / len(self.score_list)
    
    def display_score(self):
        average = self.get_average_score()
        print(f'{self.name}の平均点: {average:.2f}点')

class Grade:
    def __init__(self, subject_list):
        self.student_list = []
        self.subject_list = subject_list

    def add_student(self, student):
        self.student_list.append(student)

    def get_high_score(self, student_list, subject_list):
        highest_avg_student = max(self.student_list, key=lambda student: student.get_average_score())
        highest_avg = highest_avg_student.get_average_score()
        print(f'最高平均点の生徒: {highest_avg_student.name} - 平均点: {highest_avg:.2f}点')
    
