import sys
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = list(map(int, input().split()))
a -= 1
b -= 1
ctr = 1
for i in range(arr[a] - 1):
    b += 1
    if (b == 7):
        b = 0
        ctr += 1
print(ctr)