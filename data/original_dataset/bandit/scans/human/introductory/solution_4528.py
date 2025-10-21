a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    t = x * 60 + y
    print(24*60 - t)