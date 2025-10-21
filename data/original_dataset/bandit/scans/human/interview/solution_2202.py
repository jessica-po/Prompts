#http://codeforces.com/contest/958/problem/C1

N,p=list(map(int,input().split()))
A=list(map(int,input().split()))
sum1=A[0]
sum2=sum(A[1:])
ans=(sum1%p)+(sum2%p)
for i in range(1,N-1):
    sum1+=A[i]
    sum2-=A[i]
    ans1=sum1%p
    ans2=sum2%p
    ans=max(ans1+ans2,ans)
print(ans)