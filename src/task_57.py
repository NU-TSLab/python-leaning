import sys , itertools
def enzan(n , a):
    m = n[0]
    for i in range(3):
        if a[i] == "+":
            m = m + n[i + 1]
        if a[i] == "-":
            m = m - n[i + 1]
        if a[i] == "*":
            m = m * n[i + 1]
        if a[i] == "/":
            m = m / n[i + 1]
    return m

def b(nums):
    enzansi = ['+', '-', '*', '/']
    for i in itertools.permutations(nums):
        for j in itertools.product(enzansi , repeat=3):
            if enzan(i , j) == 10:
                print(f"{i[0]} {j[0]} {i[1]} {j[1]} {i[2]} {j[2]} {i[3]} = 10")

if len(sys.argv) == 5:
    b(list(map(int, sys.argv[1:5])))
else:
    print("4つの整数を入力してください。")