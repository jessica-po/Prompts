from math import sqrt

a, b, c = list(map(int, input().split()))
# a, b, c = 2, 5, 3

V1 = a ** 3 * sqrt(2) / 12
V2 = sqrt(2) * (b ** 3) / 6
V3 = ((5 + sqrt(5)) / 24) * (c ** 3)

print(V1 + V2 + V3)