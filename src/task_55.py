import sys

def prime_factors(n):
    factors={}
    while n%2==0:
        factors[2]=factors.get(2,0)+1
        n=n//2

    i=3
    while i*i<=n:
        while n%i==0:
            factors[i]=factors.get(i,0)+1
            n=n//i
        i=i+2

    if n>1:
        factors[n]=factors.get(n,0)+1
    
    return factors

number=int(sys.argv[1])
factors=prime_factors(number)

result = '+'.join([f'{factor}^{count}' for factor, count in factors.items()])
print(f"素因数分解：{result}")