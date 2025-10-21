n = int(input())
l = list(map(int, input().split()))
f1 = l[2]
l.sort()
f2 = l[0]
print(2 + (f1 ^ f2))