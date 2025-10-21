n = int(input())
dn = list(map(int, input().split()))
dn.sort()
a = dn[n // 2 - 1]
b = dn[n // 2]

print((b-a))