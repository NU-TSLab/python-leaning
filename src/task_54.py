import shutil

with open('./data/source.txt','w') as file:
    file.write('Since I studied "dictionary" section, understanding programming languages have been really difficult for me. I just want to play video games...')

shutil.copy('./data/source.txt','./data/destination.txt')
print('コピー完了')