n,m = map(int,input().split())
res = [0] * n
a = list(map(int,input().split()))
for i in a:
    res[i - 1] += 1
print(min(res))