number = int(input())
a = []

while number % 2 == 0:
    a.append(2)
    number //= 2

f = 3
while f * f <= number:
    if number % f == 0:
        a.append(f)
        number //= f
    else:
        f += 2

if number != 1:
    a.append(number)

temp = a[0]
count = 1
for i in range(1, len(a)):
    if a[i] == temp:
        count += 1
    else:
        print(f"{temp}^{count} *", end=" ")
        temp = a[i]
        count = 1

print(f"{temp}^{count}")