people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]

ages = [person['age'] for person in people]
print(ages)

names_over_25 = [person['name'] for person in people if person['age'] >= 25]
print(names_over_25)