list=[1,2,3,4,5,]
print(list[0])
print(list[2])
print(list[-1])
list.append(6)
print(list)
list[2]=10
print(list)
list.insert(1,10)
print(list)

'''
変数名 = [値1, 値2, …]
スライス記法：変数[開始インデックス番号: 終了インデックス：ステップ] 一部切り取ったリストを生成
変数.pop(インデックス番号)
変数.append(値)：後ろに追加
変数.insert(インデックス番号, 値)：指定した場所に追加
変数.remove(値)：削除(popはインデックスで削除)
len(変数名):カウント
変数1.extend(変数2)：結合

'''