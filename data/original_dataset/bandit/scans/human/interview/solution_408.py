a, b = list(map(int, input().split(' ')))
print(min([a, b, (a+b)//3]))