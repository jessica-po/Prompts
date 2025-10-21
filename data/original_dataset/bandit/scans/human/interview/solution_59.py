n = int(input())
a = list(map(int,input().split()))
p = input()
m = 0
suc = True
for i in range(n-1):
    m = max(m,a[i])
    if p[i] == '0' and m>(i+1):
        suc = False
        break
if suc:
    print('YES')
else:
    print('NO')