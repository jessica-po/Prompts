def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
a = li()
a.sort()
c1 = 0
p = 1
for ai in a:
    c1 += abs(ai - p)
    p += 2
c2 = 0
p = 2
for ai in a:
    c2 += abs(ai - p)
    p += 2
ans = min(c1, c2)
print(ans)