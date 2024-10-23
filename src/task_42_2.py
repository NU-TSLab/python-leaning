class Student:
    def __init__(self , name , grade):
        self.name = name
        self.grade = grade
    
def find_top_student(n):
    return print(max(n , key = lambda a: a.grade).name) #max() , lambda x: ...でdefみたいに使う。

n = [Student("田中" , 65) , Student("浜田" , 80) , Student("遠藤" , 91) , Student("松本" , 79) , Student("方正" , 55)]
print(find_top_student(n))