a = int(input())
c = list(map(int,input().split()))
summ = 0
for i in range(a):
    k = 0
    k1 = 0
    s = str(c[i])
    for x in s:
        k  = k * 100 + int(x)
    k1 = k * 10
    summ += (k + k1) * a
    summ %= 998244353
print(summ)