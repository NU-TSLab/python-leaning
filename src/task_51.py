import os

# ファイルの作成と書き込み
with open('./data/sample.txt', 'w') as file:
    file.write('Hello, World!')

# ファイルの読み込み
with open('./data/sample.txt', 'r') as file:
    content = file.read()
    print(content)

# ファイルの削除
os.remove('./data/sample.txt')