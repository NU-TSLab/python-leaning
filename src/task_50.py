import os

get=os.getcwd()
print(f"現在の作業ディレクトリ : {get}")

list=os.listdir(get)
print(f"内容 : {list}")