n,m = map(int,input().split())
box = list(map(int,input().split()))
mularr = []
queries = list(map(int,input().split()))
qm = max(queries)
cnt = 0
mularr.append([box[0],1])
candy = box[0]
for b in box[1:]:
    if b == 1:
     mularr[-1][1] +=1
    else:
     candy *= b
     mularr.append([candy,1])
    if qm <= candy:
     break
#print(mularr)
for query in queries:
    cnt = n
    test = query
    test-=1
    for k,v in mularr:
     #print(mularr[m],test)
     add = (test//k)*v
     cnt+=add
    print(cnt)