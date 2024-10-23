import os
import shutil

with open('./data/source.txt', 'w') as file:
    file.write('北陵汰')

shutil.copy('./data/source.txt','./data/destination.txt')
with open('./data/destination.txt', 'r') as file:
    content = file.read()
    print(content)