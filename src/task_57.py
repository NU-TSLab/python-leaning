import sys
import itertools
def calculate(number_list,ops):
    result=number_list[0]
    for i in range(3):
        if ops[i]=='+':
            result+=number_list[i+1]
        elif ops[i]=='-':
            result-=number_list[i+1]
        elif ops[i]=='*':
            result*=number_list[i+1]
        elif ops[i]=='/':
            if number_list[i+1]==0:
                return None
            elif number_list[i+1]!=0:
                result/=number_list[i+1]
    return result
def show(nums):
    operators=['+','-','*','/']
    for perm in itertools.permutations(nums):
        for ops in itertools.product(operators,repeat=3):
            if calculate(perm,ops)==10:
                result=f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}"
                print(f"{result}=10")
number=list(map(int,sys.argv[1:5]))
show(number)