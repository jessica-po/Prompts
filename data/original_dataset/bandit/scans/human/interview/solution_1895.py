import time

n, m =map(int, input().split())

names={None:0}

count={i:0 for i in range(1, m+1)}

a=[0]*(n+1)

for i in range(n):
    l=list(input().split())
    if l[0]=='2':
        if l[1] not in names:
            names[l[1]]=len(names)
        a[i]=names[l[1]]
        count[a[i]]=count[a[i]]+1
    # else a[i] stays 0

dense=[set() for _ in range(m+1)]

bulk=set()

# filling dense array of arrays
for i in range(n):
    if a[i]==0:
        bulk.clear()
        continue
    if a[i] in bulk: continue
    for j in bulk:
        dense[j].add(a[i])
        dense[a[i]].add(j)
    bulk.add(a[i])

res=0
happy=set()
unhappy=set()
mindep=99

independent=set()
dependent=set()
for i in range(1, m+1):
    if len(dense[i])==0: independent.add(i)
    else:
        dependent.add(i)
        if len(dense[i])<mindep:
            mindep=len(dense[i])

# print([i for i in dependent if mindep==len(dense[i])])

for k in list(dependent):
    # iterate to... too sly
    happy.clear()
    unhappy.clear()
    bulk.clear()
    bulk.update(dependent)
    happy.add(k)
    bulk.remove(k)
    for j in dense[k]:
        if j in bulk:
            unhappy.add(j)
            bulk.remove(j)

    # now making least connected happy
    while bulk:
        mini = min([len(dense[i]) for i in bulk])
        for i in list(bulk):
            if len(dense[i])==mini and (i in bulk):
                happy.add(i)
                bulk.remove(i)
                for j in dense[i]:
                    if j in bulk:
                        unhappy.add(j)
                        bulk.remove(j)
                continue

    res=max(res,len(happy))

print(res+len(independent))