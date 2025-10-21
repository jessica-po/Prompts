n = int(input())
a = 0
b = 0
for x in input().split():
    x = int(x)
    if x % 2 == 0:
        a += 1
    else:
        b += 1
res = b
if a < b:
    res = a + (b-a)//3
print(res)