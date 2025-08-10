file = open('temp.txt', 'w')
file.write('test text')
file.close()

file = open('temp.txt', 'r')
print(file.read())
file.close()
