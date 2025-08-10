data = open("multilines.txt", "w")
lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
for i in range(5):
    data.write(lines[i])

data.close()

data = open("multilines.txt", "r")
for i in range(5):
    print(data[i])

data.close()