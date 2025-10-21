n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))

mx = max(a) + m



while m:
    for i in range(n):
        if a[i] == min(a):
            a[i] += 1
            m -= 1
            break

print(max(a), mx)