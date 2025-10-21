import sys
n=int(input())
f={
 'AND':(lambda a:a[0]&a[1]),
 'OR':(lambda a:a[0]|a[1]),
 'XOR':(lambda a:a[0]^a[1]),
 'NOT':(lambda a:a[0]^1),
}
g={'0':(lambda a:0), '1':(lambda a:1)}
d=[(g[v[0]],[]) if o=='IN' else (f[o],[int(a)-1 for a in v]) for o,*v in map(str.split,sys.stdin.read().strip().split('\n'))]
t=[0]
for i in t:
 t.extend(d[i][1])
v=[0 for _ in range(n)]
for i in t[::-1]:
 o,a=d[i]
 v[i]=o([v[x] for x in a])
f=[0 for _ in range(n)]
f[0]=1
for i in t:
 if f[i]<1: continue
 o,a=d[i]
 b=[v[x]for x in a]
 assert o(b)==v[i]
 for j,k in enumerate(a):
  b[j]^=1
  f[k]=(o(b)!=v[i])
  b[j]^=1
print(''.join(str(f[i]^v[0]) for i in range(n) if not d[i][1]))