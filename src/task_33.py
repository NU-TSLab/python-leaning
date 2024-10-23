# 辞書の作成
fruit_dict = {'apple': 3, 'banana': 2, 'orange': 5}

# 1. 'banana' の値を取得する
print(fruit_dict['banana'])  # 2

# 2. 新しい要素 'grape': 4 を追加する
fruit_dict['grape'] = 4
print(fruit_dict)  # {'apple': 3, 'banana': 2, 'orange': 5, 'grape': 4}

# 3. 'apple' の値を 5 に更新する
fruit_dict['apple'] = 5
print(fruit_dict)  # {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 4}

# 4. 全てのキーを取得する
print(fruit_dict.keys())  # dict_keys(['apple', 'banana', 'orange', 'grape'])

# 5. 全ての値を取得する
print(fruit_dict.values())  # dict_values([5, 2, 5, 4])