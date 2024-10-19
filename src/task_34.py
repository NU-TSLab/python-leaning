people=[{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Doe', 'age': 22}]
age_list=[p['age'] for p in people]
#リストperson内の辞書を変数pとする。リスト内包表記
#p['age']: 各辞書 p から 'age' キーに対応する値を取得してる
print(age_list)

nijyugoijyo=[p['name'] for p in people if p['age']>=25]
print(nijyugoijyo)