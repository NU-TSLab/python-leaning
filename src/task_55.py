import sys
from collections import Counter

def prime_factorization(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)
    return factors

def format_factors(factors):
    factor_counts = Counter(factors)
    return " × ".join([f"{factor}^{count}" for factor, count in factor_counts.items()])

prime_factor = prime_factorization(int(sys.argv[1]))
factor_result = format_factors(prime_factor)
print(f"{sys.argv[1]} = {factor_result}")
