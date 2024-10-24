import sys
import itertools

numbers=list(map(int, input().split()))
print(f"入力された整数: {numbers}")#確認
#numbers_P=list(itertools.permutations(numbers))4P4
#for p in numbers_P:
   # print (p) #確認

enzanshi=['+', '-', '*', '/']
enzanshi_P=list(itertools.product(enzanshi,repeat=3))#4P3

for enzP in enzanshi_P:
    join_P=f"{numbers[0]} {enzP[0]} {numbers[1]} {enzP[1]} {numbers[2]} {enzP[2]} {numbers[3]}"
        #print(join_P)
    try:
        result=eval(join_P)
        if result==10:
            print(f"{join_P}={result}")
    except ZeroDivisionError:
            continue