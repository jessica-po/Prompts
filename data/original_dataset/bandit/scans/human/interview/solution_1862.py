read = lambda: map(int, input().split())
n = int(input())
a = list(read())
was = [0] * (n + 1)
bal = ans = 0
for i in a:
    if was[i]:
        bal -= 1
    else:
        bal += 1
        was[i] = 1
    ans = max(ans, bal)
print(ans)