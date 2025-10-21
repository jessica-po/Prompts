n = int(input())
res = -float('inf')
for _ in range(n):
    a,b = list(map(int,input().split()))
    res = max(res,a+b)
print(res)