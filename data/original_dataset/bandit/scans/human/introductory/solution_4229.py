n = int(input())
ans = 0
for i in range(n):
    if (i+1) %3 > 0 and (i+1)%5 > 0:
        ans += i+1
print(ans)