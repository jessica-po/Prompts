from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    newList = sorted(l)
    m = newList[0]
    div = newList[0]
    for i in range(n):
        if l[i]!=newList[i]:
            div = gcd(div,l[i])
    if div%m==0:
        print("YES")
    else:
        print("NO")