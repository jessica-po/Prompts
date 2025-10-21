n = int(input())
x = 0
cur = 1
lst = 1
while cur + lst <= n:
    cur, lst = cur + lst, cur
    x += 1
print(x)