n, m = map(int, input().split())
if m <= 1:
    print(1)
    return
print(min(m, n - m))