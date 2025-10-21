n = int(input())
a = [int(x) for x in input().split()]
a.sort()
num = 0
res = 0
for i in range(n):
    if int(a[i]) >= num:
        res += 1
        num += int(a[i])
    #print(res, a[i])
print(res)