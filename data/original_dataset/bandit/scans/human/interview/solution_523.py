n, m = map(int, input().split())

p = ''
q = []

arr = [input() for __ in range(n)]
s = set(arr)
for z in arr:
    if z == z[::-1]:
        p = z
    else:
        if z not in s: continue
        if z[::-1] in s:
            s.remove(z)
            s.remove(z[::-1])
            q += z,

res = ''.join(q)
res = res + p + res[::-1]
print(len(res))
print(res)