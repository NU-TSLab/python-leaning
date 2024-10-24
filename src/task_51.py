import os
with open("./data/sample.txt" , "w") as file:
    file.write("Hello , World!!")

with open("./data/sample.txt" , "r") as file:
    print(file.read())