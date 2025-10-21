t = int(input())
for i in range(t):
    a = int(input())
    if a >= 4:
        print(a % 2)
    else:
        print(4 - a)