n,k = map(int, input().split())
s = input()
ls = sorted(list(set(s)))
if k > n:
    ans = s + ''.join([ls[0] for i in range(k-n)])
    print(ans)
    return
c = len(ls)
d = {}
for i in range(c):
    d[ls[i]] = i
ns = []
for i in range(k-1,-1,-1):
    ns.append(d[s[i]])
r = 1
ans = []
for i in range(k):
    ans.append((ns[i] + r)% c)
    r = (ns[i] + r) // c
ans = list(reversed(ans))
print(''.join([ls[i] for i in ans]))