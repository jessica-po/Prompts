k = int(input())
dk = list(map(int,input().split()))
ans = []
if 0 in dk:
    ans.append(0)
if 100 in dk:
    ans.append(100)
f1 = False
for q in dk:
    if 0<q<10:
        ans.append(q)
        f1 = True
        break
f2 = False
for q in dk:
    if 9<q<100 and q%10==0:
        ans.append(q)
        f2  = True
        break
if (not f1 and not f2):
    for j in dk:
        if j!=0 and j!=100:
            ans.append(j)
            break
print(len(ans))
print(*ans)