import os

with open('./data/multilines.txt','w') as file:
    lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
    for line in lines:
        file.write(line + '\n' )

with open('./data/multilines.txt','r') as file:
    read=file.read()
    print(read)
