people = [{'name': 'John', 'age': 25}, {'name': 'Jame', 'age': 30}, {'name': 'Doe', 'age': 22}]
ages = [person['age'] for person in people]
print(ages)
name25 = [person['name'] for person in people if person['age'] >= 25]
print(name25)