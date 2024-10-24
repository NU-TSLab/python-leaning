import sys
import itertools


def keisan(list_keisan, operators):
    result = list_keisan[0]
    for i in range(3):
        if operators[i] == '+':
            result += list_keisan[i+1]
        elif operators[i] == '-':
            result -= list_keisan[i+1]
        elif operators[i] == '*':
            result *= list_keisan[i+1]
        elif operators[i] == '/':
            if list_keisan[i+1] == 0:
                return None
            result /= list_keisan[i+1]
    return result


def tannsaku(numbers):
    operators = ['+', '-', '*', '/']
    for num_permutation in itertools.permutations(numbers):
        for op_combination in itertools.product(operators, repeat=3):
            if keisan(num_permutation, op_combination) == 10:
                print(f"{num_permutation[0]} {op_combination[0]} {num_permutation[1]} {
                      op_combination[1]} {num_permutation[2]} {op_combination[2]} {num_permutation[3]} = 10")


numbers = list(map(int, sys.argv[1:5]))

tannsaku(numbers)
