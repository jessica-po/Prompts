def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

# A. Company Merging
n = ii()
c = []
for i in range(n):
    a = li()[1:]
    c.append(a)
mx = max(max(e) for e in c)
ans = sum((mx - max(e)) * len(e) for e in c)
print(ans)