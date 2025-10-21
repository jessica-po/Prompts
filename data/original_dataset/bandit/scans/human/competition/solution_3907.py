import itertools

def f(n):
    return n * (n - 1) / 2 + 1 if n % 2 else n * (n - 1) / 2 + n / 2

n, m = list(map(int, input().split()))
table = sorted([int(input().split()[1]) for _ in range(m)], reverse = True)
ans = 1
while f(ans) <= n:
    ans += 1
ans -= 1
print(list(itertools.accumulate(table))[min(ans - 1, m - 1)])