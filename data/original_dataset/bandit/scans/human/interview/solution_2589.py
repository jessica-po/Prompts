t = int(input())

for loop in range(t):

    n,x = list(map(int,input().split()))
    a = list(map(int,input().split()))

    ss = sum(a)

    if ss % x != 0:
        print (n)
    else:

        ans = -1
        for i in range(n):

            if a[i] % x != 0:
                ans = n-i-1
                break

        for i in range(n-1,-1,-1):

            if a[i] % x != 0:
                ans = max(ans , i)
                break

        print (ans)