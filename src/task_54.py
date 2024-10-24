import shutil

with open("./data/source.txt", "w") as file:
    file.write("静夜思\n床前明月光，疑是地上霜。\n举头望明月，低头思故乡。\n")

#コピー
shutil.copyfile("./data/source.txt", "./data/destination.txt")
print("ファイルをコピーしました。")

with open("./data/destination.txt", "r") as file:
    content = file.read()
    print(content)

'''
File copied.
静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
'''
