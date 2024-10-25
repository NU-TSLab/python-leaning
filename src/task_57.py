import sys
import itertools

def keisann(a, operators):
    result = a[0]
    for i in range(3):
        next_a = a[i + 1]
        operator = operators[i]
        
        if operator == '+':
            result += next_a
        elif operator == '-':
            result -= next_a
        elif operator == '*':
            result *= next_a
        elif operator == '/':
            if next_a == 0:
                return None
            result /= next_a
    return result

def kumi(numbers):
    operator_list = ['+', '-', '*', '/']

    for n in itertools.permutations(numbers):
        for op in itertools.product(operator_list, repeat=3):
            result = keisann(n, op)
            if result is not None and abs(result - 10) < 1e-9:
                expression = f"{n[0]} {op[0]} {n[1]} {op[1]} {n[2]} {op[2]} {n[3]}"
                print(f"{expression} = 10")

if len(sys.argv) < 5:
    print("4つの整数を指定してください。")
    sys.exit(1)

input_numbers = [int(arg) for arg in sys.argv[1:5]]

kumi(input_numbers)



