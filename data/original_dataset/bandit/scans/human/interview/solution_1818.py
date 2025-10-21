3

mem = [-1] * 100000

def f(x):
    if x == 0:
        return 0
    if x < 100000 and mem[x] != -1:
        return mem[x]
    if x % 2 == 0:
        res = f(x // 2)
    else:
        res = f((x - 1) // 2) + 1
    if x < 100000:
        mem[x] = res
    return res

n = int(input())
a = list(map(int, input().split()))
cnt = {}
for v in a:
    k = f(v)
    cnt[k] = cnt.get(k, 0) + 1
print(sum([v * (v - 1) // 2 for v in list(cnt.values())]))