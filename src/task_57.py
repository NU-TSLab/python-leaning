import sys


def soinnsuu(n):
    suuti = {}
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            suuti[i] = suuti.get(i, 0) + 1
            n //= i
    if n > 1:
        suuti[n] = 1
    return suuti


number = int(sys.argv[1]) if len(sys.argv) > 1 else 200

suuti = soinnsuu(number)
result = '+'.join([f'{p}' if c == 1 else f'{p}^{c}' for p, c in suuti.items()])
print(result)
