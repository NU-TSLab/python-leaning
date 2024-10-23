import sys

def prime_factors(n):
    factors = {}
    # 2で割り続ける
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # 奇数で割り続ける
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    # 最後の素数が残った場合
    if n > 2:
        factors[n] = 1
    return factors

if __name__ == "__main__":
    # コマンドライン引数が指定されているか確認
    if len(sys.argv) != 2:
        print("使用法: python task_55.py [数値]")
        sys.exit(1)

    try:
        # コマンドライン引数から数値を取得
        number = int(sys.argv[1])

        if number < 2:
            print("2以上の整数を入力してください。")
            sys.exit(1)

        # 素因数分解
        factors = prime_factors(number)

        # 結果のフォーマット
        result = ' + '.join([f'{factor}^{count}' for factor, count in factors.items()])
        
        # 出力形式を指定
        print(f"入力: {number}")
        print(f"出力: {result}")

    except ValueError:
        print("有効な整数を入力してください。")
