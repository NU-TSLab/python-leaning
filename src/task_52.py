import os

lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]

with open('./data/multilines.txt', 'w') as file:
    for line in lines:
        file.write(line)

with open('./data/multilines.txt', 'r') as file:
    content = file.read()
    print(content)
