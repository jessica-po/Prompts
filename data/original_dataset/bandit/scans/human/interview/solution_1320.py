read = lambda: list(map(int, input().split()))
n = int(input())
a = [input() for i in range(n)]
f = lambda x: x * (x - 1) // 2
cnt = 0
for i in range(n):
    k1 = a[i].count('C')
    k2 = sum(a[j][i] == 'C' for j in range(n))
    cnt += f(k1) + f(k2)
print(cnt)