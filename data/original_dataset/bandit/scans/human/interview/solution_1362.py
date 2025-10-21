n, p, m = input().split()
n = int(n)
p = int(p)
m = int(m)

ans = 0
curb = 0
curd = 1
for i in range(0, n):
    #print(curb)
    tday, tplus = input().split()
    tday = int(tday)
    tplus = int(tplus)
    if curb < 0:
        ans += (tday - curd)
        curb -= p * (tday - curd)
    elif curb - p * (tday - curd) < 0:
        curb -= p * (tday - curd)
        x = -curb
        xx = x // p
        if xx * p < x:
            xx += 1
        x = xx
        ans += x
    else:
        curb -= p * (tday - curd)
    curd = tday
    #print(curb)
    curb += tplus

tday = m + 1
if curb < 0:
    ans += (tday - curd)
    curb -= p * (tday - curd)
elif curb - p * (tday - curd) < 0:
    curb -= p * (tday - curd)
    x = -curb
    xx = x // p
    if xx * p < x:
        xx += 1
    x = xx
    ans += x

print(ans)