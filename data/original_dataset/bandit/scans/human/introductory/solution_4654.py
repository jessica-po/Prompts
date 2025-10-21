t=int(input())
for i in range (t):
    n,k=map(int,input().split())
    if n-k+1>0 and (n-k+1)%2==1:
        print("YES")
        print(*([1]*(k-1)), n-k+1)
    elif n-k*2+2>0 and (n-k*2+2)%2==0:
        print("YES")
        print(*([2]*(k-1)), n-k*2+2)
    else:
        print("NO")