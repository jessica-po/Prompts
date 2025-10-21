input()
num = list(map(int, input().split()))
maxn = 0
l, r = 0, len(num)-1
j1, j2 = num[l], num[r]
while l < r:
    if j1 == j2:
        maxn = max(j1, maxn)
        l += 1
        j1 += num[l]
    elif j1 < j2:
        l += 1
        j1 += num[l]
    else:
        r -= 1
        j2 += num[r]
print(maxn)