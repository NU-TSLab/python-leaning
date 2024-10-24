import sys  # sysモジュールをインポートして、コマンドライン引数を処理する

def prime_factors(n):
    # 素因数を格納する辞書を初期化
    factors = {}
    
    # 2で割り続ける（偶数の処理）
    while n % 2 == 0:
        # 2が素因数である場合、その指数をカウントする
        factors[2] = factors.get(2, 0) + 1 
        n //= 2  # nを2で割る
    
    # 奇数で割り続ける（3から始める）
    # nの平方根までの奇数を対象とする
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:  # nがiで割り切れる間
            # iが素因数である場合、その指数をカウントする
            factors[i] = factors.get(i, 0) + 1
            n //= i  # nをiで割る
    
    # 最後の素数が残っている場合（nが2より大きい）
    if n > 2:
        factors[n] = 1  # n自体が素数であるので、指数は1
    
    return factors  # 素因数を格納した辞書を返す

# コマンドライン引数から数値を取得
if len(sys.argv) < 2:
    # 引数が指定されていない場合のエラーメッセージ
    print("使用方法: python3 ./src/task_55.py [引数]")
    sys.exit(1)  # プログラムを終了する

# 引数から整数を取得
number = int(sys.argv[1])
# 素因数を計算する関数を呼び出す
factors = prime_factors(number)

# 結果のフォーマット
# 辞書の各素因数とその指数を「素因数^指数」の形式で結合
result = ' + '.join([f'{factor}^{count}' for factor, count in factors.items()])
print(result)  