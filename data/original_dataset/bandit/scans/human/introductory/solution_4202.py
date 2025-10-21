l, r = list(map(int, input().split()))

if (r-l)//2019 >= 1:
    print((0))
else:
    ans = float('inf')
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i != j:
                ans = min(ans, (i*j)%2019)

    print(ans)