people = [{'name':'John', 'age':25},{'name':'Jane', 'age':30},{'name':'Doe', 'age':22}]
print([person['age'] for person in people])
print([person['name'] for person in people if person['age'] > 25 ])