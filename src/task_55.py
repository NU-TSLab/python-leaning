import sys

def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1  #.get(2,0)はkeyが存在しない場合0を返す
        n //= 2
    
    for i in range(3, int(n**0.5)+1, 2):    #ある数の約数はその平方根以下にしか存在しない
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = 1
    return factors

number = int(sys.argv[1])
factors = prime_factors(number)

result = " + ".join([f"{factor}^{count}" for factor, count in factors.items()])
print(result)