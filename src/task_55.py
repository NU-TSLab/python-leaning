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

# コマンドライン引数から数値を取得
if len(sys.argv) < 2:
    print("使用方法: python3 ./task_55.py [引数]")
    sys.exit(1)

number = int(sys.argv[1])
factors = prime_factors(number)

# 結果のフォーマット
result = ' + '.join([f'{factor}^{count}' for factor, count in factors.items()])
print(result)