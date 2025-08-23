import shutil

with open('./data/source.txt','w') as file:
    file.write('Yukie')

shutil.copy('./data/source.txt','./data/destination.txt')
print("コピー完了")
