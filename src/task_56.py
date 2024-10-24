import sys
import itertools
import operator

def evaluate_expression(nums, ops):
    """演算子を使って数式を評価する"""
    result = nums[0]
    for i in range(len(ops)):
        result = ops[i](result, nums[i + 1])
    return result

def find_expressions(numbers):
    """数値の組み合わせと演算の組み合わせを探索し、結果が10になるものを表示"""
    operators = [operator.add, operator.sub, operator.mul, operator.truediv]
    operator_symbols = ['+', '-', '*', '/']

    # すべての順列を取得
    for num_perm in itertools.permutations(numbers):
        # 演算子の組み合わせを生成
        for ops in itertools.product(operators, repeat=len(numbers) - 1):
            try:
                result = evaluate_expression(num_perm, ops)
                if result == 10:
                    # 演算式を組み立てて表示
                    expression = f"{num_perm[0]}"
                    for i in range(len(ops)):
                        expression += f" {operator_symbols[operators.index(ops[i])]} {num_perm[i + 1]}"
                    print(f"式: {expression} = {result}")
            except ZeroDivisionError:
                continue  # 除算でゼロ割が発生した場合はスキップ

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <num1> <num2> <num3> <num4>")
        sys.exit(1)

    # コマンドライン引数から整数を取得
    try:
        numbers = list(map(int, sys.argv[1:5]))
        if any(num < 1 or num > 9 for num in numbers):
            print("Please enter integers between 1 and 9.")
            sys.exit(1)
    except ValueError:
        print("Please enter valid integers.")
        sys.exit(1)

    # 数値を使用して式を探索
    find_expressions(numbers)
