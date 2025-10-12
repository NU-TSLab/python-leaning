import sys
import itertools

def calclatae(num_list, ops):
    result = num_list[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += num_list[i+1]
        elif ops[i] == "-":
            result -= num_list[i+1]
        elif ops[i] == "*":
            result *= num_list[i+1]
        elif ops[i] == "/":
            if num_list[i+1] == 0:
                return None
            result /= num_list[i+1]
    return result

def find_combinations(nums):
    operators = ["+","-","*","/"]
    #全ての組み合わせを試す
    for perm in itertools.permutations(nums):
        #直積（デカルト積）：複数の集合から要素を一つずつ取り出した組み合わせ集合
        for ops in itertools.product(operators, repeat=3):
            if calclatae(perm, ops) == 10:
                print(f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]} = 10")

numbers = list(map(int, sys.argv[1:5]))
find_combinations(numbers) #