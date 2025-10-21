from sys import stdin
from sys import stdout
from collections import defaultdict
n=int(stdin.readline())
a=[map(int,stdin.readline().split(),(10,10)) for i in range(n)]
v=defaultdict(list)
for i,e in enumerate(a,1):
    q,f=e
    v[q-f].append(i)
    v[q+f-1].append(-i)
sa=set()
rez=0
for j in sorted(v.keys()):
    for d in v[j]:
        if d>0:
            sa.add(d)
    for d in v[j]:
        if -d in sa:
            sa.clear()
            rez+=1
stdout.write(str(rez))