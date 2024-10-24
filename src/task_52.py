lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
with open("./data/multilines.txt", 'w', encoding='utf-8') as f:
    for line in lines:
         f.writelines(line + '\n')

with open("./data/multilines.txt", 'r', encoding='utf-8') as f:
       print(f.read())