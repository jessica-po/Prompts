n = int(input())
p = -float("INF")
ans = 1
A = []
for i in range(n) :
    x, h = list(map(int, input().split()))
    A.append([x,h])
for i in range(n-1) :
    x, h = A[i]
    if x-h > p :
        ans += 1
        p = x
    elif x+h < A[i+1][0] :
        ans += 1
        p = x+h
    else :
        p = x
print(ans)