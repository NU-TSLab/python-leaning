dic = [{'name':'John', 'age':25},
       {'name':'Jane', 'age':30},
       {'name':'Doe', 'age':22}]

ages = [person['age'] for person in dic]
print(ages)
name_25 = [person['name'] for person in dic if person['age']>25]
print(name_25)