import os

#wで書き込み、rで読み込み
with open('./data/sample.txt',"w") as file:
    file.write("Hello, World!")

with open("./data/sample.txt","r") as file:
    content = file.read()
    print(content)

#ファイル削除
os.remove("./data/sample.txt")