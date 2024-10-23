fruit_dict = {'apple': 3, 'banana': 2, 'orange': 5}
#辞書の要素を取得する
print(fruit_dict["banana"])
print(fruit_dict.get("banana"))

#新しい要素の追加
fruit_dict["grape"] = 4
print(fruit_dict)
#辞書の値を変更する
fruit_dict["apple"] = 5
print(fruit_dict)  

#全てのキーを取得する
print(fruit_dict.keys())
#全ての値を取得する
print(fruit_dict.values())

"""
2
2
{'apple': 3, 'banana': 2, 'orange': 5, 'grape': 4}
{'apple': 5, 'banana': 2, 'orange': 5, 'grape': 4}
dict_keys(['apple', 'banana', 'orange', 'grape'])
dict_values([5, 2, 5, 4])
"""