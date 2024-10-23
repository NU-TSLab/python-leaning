#名前を引数として受け取り、"Hello, [名前]!" という挨拶を出力する関数greetを作成
def greet(name):
    print(f'Hello, {name}!')

input_name = input('名前を入力してください:')
greet(input_name)

'''
名前を入力してください:LIN
Hello, LIN!
'''