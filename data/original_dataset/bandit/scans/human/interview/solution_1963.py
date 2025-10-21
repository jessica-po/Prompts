n = int(input()) + 1
t = [1] + list(map(int, input().split())) + [1]
p = [True] * n
s, q = 0, list(range(1, n))
for i in range(1, n):
    if p[i]:
        a = b = i
        d = t[i]
        if d == 1: 
            s, q = n - 2, [1]
            break
        while t[a - 1] % d == 0: a -= 1
        while t[b + 1] % d == 0:
            b += 1
            p[b] = False
        d = b - a
        if d > s: s, q = d, [a]
        elif d == s != 0: q.append(a)
print(len(q), s)
print(' '.join(map(str, q)))