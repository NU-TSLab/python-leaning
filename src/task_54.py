import shutil

with open("./data/source.txt", "w") as file:
    file.write("This is the source file.")

shutil.copyfile("./data/source.txt", "./data/destination.txt")
print("ファイルをコピーしました")