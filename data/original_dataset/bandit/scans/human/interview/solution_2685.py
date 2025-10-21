# cook your dish here
def ans(n,a,b):
    if n == act:
        return 0
    if dp[n][a][b] != -1:
        return dp[n][a][b]
    if l[n] == "0":
        dp[n][a][b]
        return ans(n+1,a+1,b)
    elif l[n] == "1":
        dp[n][a][b] = ans(n+1,a,b+1)
        return ans(n+1,a,b+1)
    elif l[n] == "?":
        dp[n][a][b] = min((a-l1[n]+1)*x -(a+1) + ans(n+1,a+1,b),(b-l2[n]+1)*y -(b+1) + ans(n+1,a,b+1))
        return(min((a-l1[n]+1)*x -(a+1) + ans(n+1,a+1,b),(b-l2[n]+1)*y -(b+1) + ans(n+1,a,b+1)))
    else:
        dp[n][a][b] = ans(n+1,a,b)
        return ans(n+1,a,b)

l = str(input())
x,y = map(int,input().split())
dp = [[[-1 for i in range(101)]for j in range(101)]for k in range(101)]
l1 = []
l2 = []
c = 0
k = 0
for i in l:
    if i == "1":
        c+=1
    if i == "0":
        k+=1
    l1.append(k)
    l2.append(c)
act = len(l)
dd = ans(0,0,0)
print(dd)