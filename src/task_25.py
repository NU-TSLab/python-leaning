num = int(input("数値を入力してください: "))
if num < 0:
    print("負数です")
elif num % 2 == 0:
    print("偶数です")
else:
    print("奇数です")