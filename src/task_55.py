
num = int(input())

def soinsubunkai(n):
    dic = {}  
    #値に数字、キーに指数

    count = 0
    while n % 2 == 0:
        n = n//2
        count += 1
    if count > 0:
        dic[2] = count
    
    for i in range(3, n + 1, 2):
        count = 0
        while n % i == 0:
            n = n//i
            count += 1
        if count > 0:
            dic[i] = count
    return dic

def format(dic):
    result = []
    for prime, sisu in dic.items():
        result.append(f"{prime}^{sisu}")
    return " + ".join(result)



if num <= 1:
    print(f"{num}は素数ではありません")
else:
    dic = soinsubunkai(num)
    result = format(dic)
    print(f"{result}")
