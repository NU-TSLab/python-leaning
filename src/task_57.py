import itertools
import operator
import sys

# 四則演算の定義
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# 演算結果が10になるかを探索する関数
def find_expression(numbers):
    # 全ての順列を取得
    for perm in itertools.permutations(numbers):
        # 全ての演算子の組み合わせを取得
        for op_comb in itertools.product(ops.keys(), repeat=3):
            # 3つの数式を作る
            expr1 = f"(({perm[0]} {op_comb[0]} {perm[1]}) {op_comb[1]} {perm[2]}) {op_comb[2]} {perm[3]}"
            expr2 = f"({perm[0]} {op_comb[0]} ({perm[1]} {op_comb[1]} {perm[2]})) {op_comb[2]} {perm[3]}"
            expr3 = f"{perm[0]} {op_comb[0]} ({perm[1]} {op_comb[1]} ({perm[2]} {op_comb[2]} {perm[3]}))"
            expr4 = f"{perm[0]} {op_comb[0]} (({perm[1]} {op_comb[1]} {perm[2]}) {op_comb[2]} {perm[3]})"
            expr5 = f"({perm[0]} {op_comb[0]} {perm[1]}) {op_comb[1]} ({perm[2]} {op_comb[2]} {perm[3]})"
            
            # 各数式を評価して結果が10か確認
            for expr in [expr1, expr2, expr3, expr4, expr5]:
                try:
                    if eval(expr) == 10:
                        print(f"式: {expr} = 10")
                except ZeroDivisionError:
                    continue

if __name__ == "__main__":
    # コマンドライン引数から4つの整数を取得
    if len(sys.argv) != 5:
        print("4つの整数を入力してください。")
        sys.exit(1)
    
    try:
        numbers = list(map(int, sys.argv[1:5]))
    except ValueError:
        print("入力は整数である必要があります。")
        sys.exit(1)

    # 結果が10になる式を探す
    find_expression(numbers)
