import sys
import itertools

def calculate(num_list, ops):
   
    nums = list(num_list)
    operators = list(ops)

   
    i = 0
    while i < len(operators):
        if operators[i] in ('*', '/'):
            a = nums[i]
            b = nums[i + 1]
            if operators[i] == '*':
                nums[i] = a * b
            else:  # '/'
                if b == 0:
                    return None
                nums[i] = a / b
            del nums[i + 1]
            del operators[i]
        else:
            i += 1

    
    result = nums[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += nums[i + 1]
        else:
            result -= nums[i + 1]

    return result

def find_combinations(nums):
    operators = ['+', '-', '*', '/']
    found = False
    for perm in itertools.permutations(nums):
        for ops in itertools.product(operators, repeat=3):
            if calculate(perm, ops) == 10:
                print(f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]} = 10")
                found = True
    if not found:
        print("10になる組み合わせは見つかりませんでした。")



numbers = list(map(int, sys.argv[1:5]))
find_combinations(numbers)
