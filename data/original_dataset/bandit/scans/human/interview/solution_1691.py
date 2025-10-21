n, m = [int(i) for i in input().split()]
if m > n//2:
    m = n-m
ans = [1]
count = 0
c = 1
for i in range(n):
    count+=m
    if count>n:
        c+=1
        count-=n
        ans.append(ans[-1] +c)
        c+=1
    else:
        ans.append(ans[-1] +c)
ans = ans[1:]
print(*ans)