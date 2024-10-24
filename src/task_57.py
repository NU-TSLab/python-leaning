import sys
from itertools import permutations, product

def make10(nums):
    found = False
    for p in permutations(nums):
        for ops in product('+-*/', repeat=3):
            expr = f"{p[0]}{ops[0]}{p[1]}{ops[1]}{p[2]}{ops[2]}{p[3]}"
            try:
                if eval(expr) == 10:
                    print(f"{expr} = 10")
                    found = True
                    break
            except:
                continue
        if found:
            break
    if not found:
        print("解が見つかりませんでした")

nums = [int(x) for x in sys.argv[1:5]]
make10(nums)
