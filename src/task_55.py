import sys
def prime(n):
    factors={}
    while n%2==0:
        factors[2]=factors.get(2,0)+1
        n//=2
    i=3
    while i*i<=n:
        while n%i==0:
            factors[i]=factors.get(i,0)+1
            n//=i
        i=i+2
    if n>2:
        factors[n]=1
    return factors
number=int(sys.argv[1])
factors=prime(number)
result="+".join(f'{factor}^{count}' for factor,count in factors.items())
print(result)