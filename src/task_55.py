import sys
n = int(sys.argv[1])
m = []  
a = 2
while n > 1:
    while n % a == 0:
        m.append(a)
        n = n // a
    a = a + 1
print(" + ".join([f"{i}^{m.count(i)}" if m.count(i) > 1 else str(i) for i in sorted(set(m))]))