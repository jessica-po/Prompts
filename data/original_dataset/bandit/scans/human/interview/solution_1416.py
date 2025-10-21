n, w = list(map(int, input().split()))
a = sorted(map(int, input().split()))

x = min(min(a[:n]), min(a[n:]) / 2)
print(min(w, 3 * n * x))