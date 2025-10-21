n = int(input())
x = list(map(int,input().split()))

y = sorted(x)

ans1 = y[n//2]
ans2 = y[n//2-1]

for i in x :
    if i < ans1 :
        print(ans1)
    else :
        print(ans2)