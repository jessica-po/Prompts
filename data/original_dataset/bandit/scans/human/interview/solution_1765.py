n = int(input())
a = list(map(int, input().split()))

mxa = max(a)
v = 1 << 30
while v > mxa:
    v >>= 1

while True:
    d = -1
    for i in range(n):
        if a[i] & v:
            d &= a[i]
    if d % v == 0:
        break
    v >>= 1

b = [i for i in a if i & v]
print(len(b))
print(' '.join(map(str,b)))