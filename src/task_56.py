import csv

class Student:
    def __init__(self, name, score_list):
        self.name = name
        self.score_list = score_list

    def get_avarage_score(self, score_list):
        return sum(self.score_list) / len(self.score_list)
    
    def display_score(name, score_list):
        print(name, end=" ")
        for i in range(len(score_list) - 1):
            print(score_list[i], end=" ")

        print(score_list[len(score_list)])

class Grade:
    def __init__(self, student_list, subject_list):
        self.student_list = student_list
        self.subject_list = subject_list
        self.maxnum = -1
        self.maxstudent = -1

    def get_high_score(self, student_list, subject_list):
        for i in range(len(student_list)):
            if self.maxnum >= Student.score_list:
                self.maxnum = Student.score_list
                self.maxstudent = i

        return student_list[self.maxnum]
    
csv_data = []
