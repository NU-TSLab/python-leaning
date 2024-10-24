import sys
import itertools

def calculate(num_list, ops):
    """演算子を使って数式を評価する"""
    if not num_list:  # 空のリストをチェック
        return None
    
    result = num_list[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += num_list[i + 1]
        elif ops[i] == '-':
            result -= num_list[i + 1]
        elif ops[i] == '*':
            result *= num_list[i + 1]
        elif ops[i] == '/':
            if num_list[i + 1] != 0:
                result /= num_list[i + 1]
            else:
                return None  # ゼロ除算を避ける
    return result

def find_combinations(numbers):
    """数値の組み合わせと演算の組み合わせを探索し、結果が10になるものを表示"""
    operators = ['+', '-', '*', '/']

    # すべての順列を取得
    for perm in itertools.permutations(numbers):
        # 演算子の組み合わせを生成
        for ops in itertools.product(operators, repeat=len(numbers) - 1):
            result = calculate(perm, ops)
            if result == 10:
                # 演算式を組み立てて表示
                expression = f"{perm[0]}"
                for i in range(len(ops)):
                    expression += f" {ops[i]} {perm[i + 1]}"
                print(f"式: {expression} = {result}")

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
    find_combinations(numbers)
