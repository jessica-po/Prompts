T = int(input())

for _ in range(T):
    s = input()
    n = len(s)
    res = 10 ** 100
    for i in range(n + 1):
        p,q = s[:i], s[i:]
        res = min(res, p.count('0') + q.count('1'))
        res = min(res, p.count('1') + q.count('0'))
    print(res)