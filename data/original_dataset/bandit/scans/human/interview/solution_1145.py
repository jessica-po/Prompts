n = int(input())
A = list(map(int, input().split()))
A.sort()
prev = -1
res = 0

for x in A:
    if x > prev:
        prev = x
    else:
        prev = prev + 1
        res += prev - x
print(res)