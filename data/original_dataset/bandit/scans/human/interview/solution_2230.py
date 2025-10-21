n = int(input())
l = 0
r = n * n - 1

for i in range(n):
    for k in range(n // 2):
        print(l + 1, end = ' ')
        print(r + 1, end = ' ')
        l += 1
        r -= 1
    print()