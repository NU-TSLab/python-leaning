lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]

# 書き込み
with open('./data/multilines.txt', 'w') as file:
    file.writelines(lines)

# 読み込み
with open('./data/multilines.txt', 'r') as file:
    content = file.read()
    print(content)