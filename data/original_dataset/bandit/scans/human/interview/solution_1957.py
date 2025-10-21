n, a, b = [int(x) for x in input().split()]

hs = [int(x) for x in input().split()]

target = 1.0 * hs[0] * a / b

left = sorted(hs[1:])
s = sum(hs)

res = 0
while s > target:
    res += 1
    s -= left[-res]

print(res)