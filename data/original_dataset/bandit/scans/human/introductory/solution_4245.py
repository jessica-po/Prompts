import math
a, b = list(map(int, input().split()))
print(math.ceil((b-a)/(a-1)) + 1)