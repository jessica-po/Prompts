n = int(input())

data = []

for i in range(n):
    a, b = list(map(int, input().split()))
    data.append([a, b])


ans  = True
prev = max(data[0])
for i in range(1, n):
    a, b = data[i]
    a, b = min(a, b), max(a,b)
    
    if a > prev:
        ans = False
        break

    if a <= prev < b:
        prev = a
        continue

    if prev >= b:
        prev = b


if ans :
    print("YES")
else:
    print('NO')