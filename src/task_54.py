import os
import shutil
with open("./data/source.txt","w") as f:
     f.write("Hello, World!")
shutil.copyfile("./data/source.txt", "./data/destination.txt")
print("ファイルのコピーが完了しました:")
