n =[{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
age = [person['age'] for person in n]
print(age)
name = [person['name'] for person in n if person['age'] >= 25]
print(name)