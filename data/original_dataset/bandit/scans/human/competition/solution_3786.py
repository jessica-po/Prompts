n = int(input())
p = [-1, 0] + [int(x) for x in input().split()]
h = [0] * (n+1)
count = [0] * n
count[0] = 1
max_h = 0
for i in range(2, n+1):
    h[i] = h[p[i]]+1
    count[h[i]]+=1
    max_h = max(max_h,h[i])
ans = 0
for i in range(max_h+1):
    ans += count[i]%2
print(ans)