n,d=list(map(int,input().split()))

A=list(map(int,input().split()))

m=int(input())

A.sort()

if(m<=n):
    print(sum(A[:m]))

else:
    print(sum(A)-(d*(m-n)))