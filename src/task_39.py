def sum_numbers(*args):
    total = sum(args) 
    print(f"合計は{total}です。")

sum_numbers(1,2,3,4,5)

#可変長引数