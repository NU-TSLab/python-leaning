# task_55.py
import sys

def prime_factorization(n):
    fomula = {}

    while n % 2 == 0:
        fomula[2] = fomula.get(2,0) + 1
        n //= 2

    for i in range(3,n,2):
        while n % i == 0:
            fomula[i] = fomula.get(i, 0) + 1
            n //= i

    if n > 2:
        fomula[n] = 1
    return fomula

number = int(sys.argv[1])
fomula = prime_factorization(number)

result = ' + '.join([f'{fomula}^{count}' for fomula, count in fomula.items()])
print(result)

