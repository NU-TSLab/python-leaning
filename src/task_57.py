import sys
import itertools

inputs = sys.argv[1:]#1こめ無視
numbers = [int(i) for i in inputs]
print(f"入力された整数: {numbers}")#確認

numbers_P=list(itertools.permutations(numbers))
#for p in numbers_P:
   # print (p) #確認

enzanshi=['+', '-', '*', '/']
enzanshi_P=list(itertools.product(enzanshi,repeat=3))#4P3

for numP in numbers_P:
    for enzP in enzanshi_P:
        join_P=f"{numP[0]} {enzP[0]} {numP[1]} {enzP[1]} {numP[2]} {enzP[2]} {numP[3]}"
        #print(join_P)

        try:

            result=eval(join_P)
            if result==10:
                print(f"{join_P}={result}")
        except ZeroDivisionError:
            continue






