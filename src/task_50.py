import os

import os

# 現在の作業ディレクトリを取得して表示
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# 現在の作業ディレクトリの内容をリストで表示
directory_contents = os.listdir(current_directory)
print(f"Directory contents: {directory_contents}")

#Current directory: /Users/linhaojie/python-leaning
#Directory contents: ['README.md', 'img', 'githubの使い方.md', '.git', 'data', 'src']