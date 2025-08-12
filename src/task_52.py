lines=["Line 1","Line 2","Line 3","Line 4","Line 5"]

with open('./data/multilines.txt','w') as file:
    for line in lines:
        file.write(line+'\n')

with open('./data/multilines.txt','r') as file:
    contents=file.read()
    print(contents)