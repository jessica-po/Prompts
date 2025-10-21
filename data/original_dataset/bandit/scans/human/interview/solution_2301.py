import sys
input = sys.stdin.readline

n = int(input())
x = sorted(list(map(int, input().split())))
a, b = x[:n//2], x[n//2:]
tmp = []
for i in range(n//2):
    tmp.append(b[i])
    tmp.append(a[i])
if n % 2:
    tmp.append(b[-1])
cnt = 0
for i in range(1, n-1, 2):
    if tmp[i+1] > tmp[i] < tmp[i-1]:
        cnt += 1
print(cnt)
print(*tmp)