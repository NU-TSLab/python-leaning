import sys
import itertools

def calculate(num_list,ops):
    result=num_list[0]
    for i in range(3):
        if ops[i]=='+':
            result+=num_list[i+1]
        elif ops[i]=='-':
            result-=num_list[i+1]
        elif ops[i]=='*':
            result*=num_list[i+1]
        elif ops[i]=='/':
            if num_list[i+1]==0:
                return None
            result/=num_list[i+1]
    return result

def find_combination(nums):
    operators=['+','-','*','/']
    for perm in itertools.permutations(nums):
        for ops in itertools.product(operators,repeat=3):
            if calculate(perm,ops)==10:
                print(f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}=10")

numbers=list(map(int,sys.argv[1:5]))
find_combination(numbers)