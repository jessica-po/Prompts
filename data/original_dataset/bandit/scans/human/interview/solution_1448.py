n, d = list(map(int, input().split()))

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    print(('YES' if x+y in range(d, n + n - d + 1) and x-y in range(-d, d + 1) else 'NO'));