t=int(input())
for x in range(t):
    a,b,n,m= map(int,input().split(" "))
    if a+b<n+m:
        print("No")
    else:
        if m>min(a,b):
            print("No")
        else:
            print("Yes")