import math
 
def gcdExtended(a, b):  
  
    # Base Case  
    if a == 0 :   
        return b, 0, 1
             
    gcd, x1, y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 
 
def rev_elem(x, m):
    return (gcdExtended(x, m)[1] % m + m) % m
 
n, m = map(int, input().split())
a = []
if n > 0:
    a = [int(i) for i in input().split()]
 
banned = [False] * (m + 5)
for i in a:
    banned[i] = True
 
cycle = [[] for i in range(m + 5)]
d, dp, p = [], [], []
for i in range(m):
    cycle[math.gcd(m, i)].append(i)
cycle = [[i for i in j if not banned[i]] for j in cycle]
 
d = [i for i in range(1, m + 1) if m % i == 0]
dp = [len(cycle[i]) for i in d]
p = [-1 for i in d]
ans, lst = -1, -1
 
for i in range(len(d)):
    if dp[i] > ans:
        ans, lst = dp[i], i
    for j in range(i + 1, len(d)):
        if d[j] % d[i] != 0 or dp[j] > dp[i] + len(cycle[d[j]]):
            continue
        dp[j] = dp[i] + len(cycle[d[j]])
        p[j] = i
print(ans)
        
pos, dpos, pref = [], [], []
cur = lst
while cur != -1:
    dpos.append(d[cur])
    cur = p[cur]
dpos.reverse()
 
for i in dpos:
    pref += cycle[i]
cur = 1
for i in pref:
    ad = 1
    if math.gcd(i, m) != math.gcd(cur, m):
        ad = ((cur * math.gcd(i, m) // math.gcd(cur, math.gcd(i, m))) // cur) % m
    ncur = (cur * ad) % m
    ad *= i // math.gcd(ncur, m) * (rev_elem(ncur // math.gcd(ncur, m), m // math.gcd(ncur, m)))

    ad %= m
    cur = (cur * ad) % m
 
    pos.append(ad)
 
print(*pos)