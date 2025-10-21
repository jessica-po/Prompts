for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a,b = 0,0
    arr.sort()
    for i in arr:
        if a==i:
            a+=1
        elif b==i:
            b+=1
    print(a+b)