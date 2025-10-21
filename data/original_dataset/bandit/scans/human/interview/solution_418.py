read = lambda: map(int, input().split())
n = int(input())
for i in range(n):
    name, x, y = input().split()
    x, y = int(x), int(y)
    if x >= 2400 and y > x:
        print('YES')
        return
print('NO')