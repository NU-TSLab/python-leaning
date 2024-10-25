lines= ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]

with open('C:\\Users\\itachi.2590\\python-leaning\\data\\multilines.txt', 'w') as file:
    file.writelines(lines)

with open('C:\\Users\\itachi.2590\\python-leaning\\data\\multilines.txt', 'r') as file:
    content=file.read()
    print(content)