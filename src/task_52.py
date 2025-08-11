lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]

with open('multilines.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')

with open('multilines.txt', 'r') as file:
    print(file.readlines())