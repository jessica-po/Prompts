from sys import stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

def solve(n, b):
    f = [True for i in range(2*n+1)]
    for x in b:
        if not f[x]:
            return [-1]
        f[x] = False
    a = []
    for x in b:
        a.append(x)
        for y in range(x+1, 2*n+1):
            if f[y]:
                a.append(y)
                f[y] = False
                break
        else:
            return [-1]
    return a

t, = rl()
for _ in range(t):
    print(*solve(rl()[0], rl()))