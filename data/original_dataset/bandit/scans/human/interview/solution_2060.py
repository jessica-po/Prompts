n=int(input())
for i in range(n):
    x=int(input())
    f=0
    for a in range(100):
        for b in range(100):
            if 3*a+7*b==x:
                f=1
    if f==1:
        print("YES")
    else:
        print("NO")