n = int(input())

A = [-1]
ans = [1]

for i in range(n):
    A.append(tuple(map(int, input().split())))

a = A[1][0]
b = A[1][1]

c = A[a][0]
d = A[a][1]

if b == c or b == d:
    ans.append(a)
    ans.append(b)
else:
    ans.append(b)
    ans.append(a)

while len(ans) != n:
    p = A[ans[-2]]
    
    if p[0] == ans[-1]:
        ans.append(p[1])
    else:
        ans.append(p[0])

for i in ans:
    print(i, end=' ')