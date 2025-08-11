import shutil
with open("./data/source.txt", "w") as file:
    file.write("私の名前は水島 鈴和です。")

shutil.copy('./data/source.txt', './data/destination.txt')
print('コピー完了')
