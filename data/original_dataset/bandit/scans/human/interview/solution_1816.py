k=0

d = [0] * 200005
x = int(input())
p = list(map(int, input().split(' ')))
for i in range(len(p)):
    d[p[i]] = i

for i in range(1, x):
    k += abs(d[i+1] - d[i])

print(k)