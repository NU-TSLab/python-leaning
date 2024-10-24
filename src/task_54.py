import os
import shutil
with open("./data/source.txt" , "w") as file:
    file.write("サバの味噌煮定食大盛り。")
shutil.copyfile("./data/source.txt" , "./data/destination.txt")
print("コピー完了!")