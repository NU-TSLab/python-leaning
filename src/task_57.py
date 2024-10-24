import itertools
import sys

# 数値a、bに対して演算子opを用いて計算する関数
def calc(a, b, op):
    if op == "+":
        return a + b  # 足し算
    elif op == "-":
        return a - b  # 引き算
    elif op == "*":
        return a * b  # 掛け算
    elif op == "/":
        if b != 0:
            return a / b  # 割り算（ゼロ除算のチェック）
        else:
            return None  # ゼロで割る場合はNoneを返す

# 数字の組み合わせを探索する関数
def search_combinations(numbers):
    # 四則演算の組み合わせを生成（演算子は3つ必要）
    for ops in itertools.product(["+", "-", "*", "/"], repeat=3):
        # 数字の全ての順列を生成
        for perm in itertools.permutations(numbers):
            # 演算式を文字列として構築
            expression = f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            try:
                # eval関数を用いて式を評価
                result = eval(expression)
                # 最終結果が10であるかチェック
                if result == 10:
                    return perm, ops
            except ZeroDivisionError:
                continue  # ゼロ除算が発生した場合は無視
    return None, None  # 結果が見つからない場合

# コマンドライン引数が4つ未満の場合、エラーメッセージを表示
if len(sys.argv) < 5:
    print("Usage: python3 ./src/task_57.py [number1] [number2] [number3] [number4]")
    sys.exit(1)

# コマンドライン引数から数字を取得し、整数のリストに変換
numbers = list(map(int, sys.argv[1:]))
# 演算の組み合わせを探索
perm, ops = search_combinations(numbers)
# 結果が見つからなかった場合の処理
if perm is None:
    print("No result")  # 結果がない場合
else:
    # 結果が見つかった場合、計算式を表示
    print(f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]} = 10")