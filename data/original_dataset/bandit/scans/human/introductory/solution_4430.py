n, m, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

b = k
count = 0
for obj in a[::-1]:
    if obj > k:
        break
    if obj > b:
        if m > 1:
            m -= 1
            b = k - obj
            count += 1
        else:
            break
    else:
        b -= obj
        count += 1

print(count)