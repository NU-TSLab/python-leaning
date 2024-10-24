import os
#os.makedirs("./data", exist_ok=True)
with open("./data/sample.txt", 'w', encoding='utf-8') as f:
    f.write("Hello, World!")
with open("./data/sample.txt", 'r', encoding='utf-8') as f:
    print(f.read())

#f.close()いらなかった
os.remove("./data/sample.txt")

