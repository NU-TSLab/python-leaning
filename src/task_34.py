people=[{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
all_age=[person['age'] for person in people]
print(all_age)
name_25_overs=[person['name'] for person in people if person['age']>=25]
print(name_25_overs)
