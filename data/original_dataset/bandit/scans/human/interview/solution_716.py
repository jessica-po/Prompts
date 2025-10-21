n, a, b = list(map(int, input().split()))
m = input()
if m[a - 1] == m[b - 1]:
    print(0)
else:
    print(1)