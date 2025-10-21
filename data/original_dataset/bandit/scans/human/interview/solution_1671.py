diff=0
x = int(input())
l = list(map(int, input().split(' ')))
s = sum(l)
k = s//x
knum = (k+1)*x-s
kpnum = x - knum
a = knum * [k] + [k+1] * kpnum
a.sort()
l.sort()
for i in range(len(a)):
    diff += abs(a[i]-l[i])
print(int(diff/2))