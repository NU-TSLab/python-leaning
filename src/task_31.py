ls = [1, 2, 3, 4, 5]

print(ls[0]) # 1

print(ls[2]) # 3

print(ls[-1]) # 5

ls.append(6) 
print(ls) # [1, 2, 3, 4, 5, 6]

ls.append(2) = 10
print(ls) # [1, 2, 10, 4, 5, 6]

ls.insert(1, 10)
print(ls) # [1, 10, 2, 10, 4, 5, 6]