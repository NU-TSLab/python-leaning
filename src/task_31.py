list = [1,2,3,4,5]
print(f"最初の要素: {list[0]}")
print(f"3番目の要素: {list[2]}")
print(f"最後の要素: {list[-1]}")

list.append(6)
print(f"全体: {list}")

list[2] = 10
print(f"全体: {list}")

list.insert(1, 10)
print(f"全体: {list}")

"""
linhaojie@MacBook-Air-M3 python-leaning % /usr/bin/python3 /Users/linhaojie/python-leanin
g/src/task_31.py
最初の要素: 1
3番目の要素: 3
最後の要素: 5
全体: [1, 2, 3, 4, 5, 6]
全体: [1, 2, 10, 4, 5, 6]
全体: [1, 10, 2, 10, 4, 5, 6]
"""