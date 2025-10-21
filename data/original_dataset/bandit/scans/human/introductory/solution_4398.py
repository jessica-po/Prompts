a = int(input())
p, q = input().split()

ans = ''
for i in range(a):
    ans += p[i]
    ans += q[i]
print(ans)