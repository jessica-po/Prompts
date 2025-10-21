from collections import defaultdict
def count(x):
    c=0
    while x > 0:
        c+=1
        x &= (x-1)
    return c

n,m=list(map(int,input().split()))
g=defaultdict(list)
for _ in range(m):
    u, v = list(map(int,input().split()))
    u-=1;v-=1
    g[u].append(v)
    g[v].append(u)

mask1=0;mask2=0;MAX=(1<<n)-1
a=[0]*(1 << n)
dp=[MAX]*(1 << n)
if m == (n*(n-1))//2:
    print(0)
    return
for i,j in list(g.items()):
    mask1  = (1 << i);mask2=0;mask2 |= mask1
    for k in j:
        mask2 |= (1 << k)
        
    dp[mask2]=mask1
    a[mask1]=mask2
    
for i in range(0,(1 << n)-1):
    if dp[i] != MAX:
        #print('HEllo')
        temp = dp[i] ^ i 
        for j in range(n):
            if temp & (1 << j) != 0:
                nmask = i | a[(1 << j)]
                dp[nmask]=dp[i] | (1 << j) if count(dp[i] | (1 << j)) < count(dp[nmask]) else dp[nmask]
                
ans = []
for i in range(n):
    if dp[-1] & (1 << i) != 0:
        ans.append(i+1)
print(len(ans))
print(*ans)