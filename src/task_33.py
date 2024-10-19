fruit={'apple': 3, 'banana': 2, 'orange': 5}
print(fruit.get("banana"))

fruit.setdefault('grape',4)
print(fruit)
#fruit_dict['grape'] = 4

fruit['apple']=5
print(fruit)

print(fruit.keys())

print(fruit.values())

'''
変数名.get()：値の取得
'key名' in 変数名：キーの存在確認
値 in 変数名：      値の存在確認
変数名.keys:()キー取り出し
変数名.values():値取り出し
変数名.item():キーと値の取り出し
変数名.setdefault('キー',値):要素の追加
変数名['キー']=値:上書き、追加
変数名1.update(変数名2):既存の辞書に別の辞書の要素を追加
変数名.pop('キー')
変数名.clear():全消し
変数名.copy():コピー
dict.fromkeys(コピー元変数,値の初期値)関数：キーだけコピー
sorted()関数:並びかえ(戻り値はリスト)

'''