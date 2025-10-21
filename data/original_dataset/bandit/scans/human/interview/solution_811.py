a, b = map(int, input().split())
k = a
x = 0
count = 0
while k > 0:
    k -= 1
    x += 1
    if x == b:
        x = 0
        k += 1
    count += 1
print(count)