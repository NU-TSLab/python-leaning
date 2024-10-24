import sys
from collections import Counter

def prime_factors(n):
    factors = []
    # 2で割り切れるだけ割る
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # 3以上の奇数で割り切れるだけ割る
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # 最後に残った数が素数なら追加
    if n > 2:
        factors.append(n)
    return factors

def format_factors(factors):
    #counterクラス　collectionsモジュールに含まれる
    factor_counts = Counter(factors)
    formatted = ' + '.join([f"{factor}^{count}" for factor, count in factor_counts.items()])
    return formatted

if __name__ == "__main__":
    # コマンドライン引数から数値を取得
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
    else:
        try:
            num = int(sys.argv[1])
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                factors = prime_factors(num)
                result = format_factors(factors)
                print(f"素因数分解の結果: {result}")
        except ValueError:
            print("Please enter a valid integer.")
