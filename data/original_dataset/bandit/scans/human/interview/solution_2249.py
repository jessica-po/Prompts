def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
a = li()
ans = 0
cnt = [0] * (10 ** 5 + 10)
cur = set()
for ai in a:
    cnt[ai] = len(cur)
    cur.add(ai)
ans = sum(cnt)
print(ans)