n = int(input())
min1, max1 = map(int, input().split())
min2, max2 = map(int, input().split())
min3, max3 = map(int, input().split())

d1 = min(n - min2 - min3, max1)
d2 = min(n - d1 - min3, max2)
d3 = n - d1 - d2

print(d1,d2,d3)