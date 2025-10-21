n = int(input())
a = list(map(int, input().split()))
c = 0
l = 0
b = 0
while c < len(a) and a[c] == 0:
    c += 1
    b += 1

if c == len(a):
    print(0)
    return

d = len(a) - 1
while a[d] != 1:
    d -= 1
    b += 1

while c <= d:
    if a[c] == 0:
        l += 1
    else:
        if l > 1:
            b += l
        l = 0
    c += 1

print(n - b)