from math import*
from random import*

# input = open(file = "input.txt", mode = "r")
# output = open(file = "output.txt", mode = "w")
# list(map(int, input().split()))

n = int(input())
A = list(map(int, input().split()))
z, f = 0, 0
for i in range(n):
    if A[i] == 0:
        z += 1
    else:
        f += 1
if (z == 0):
    print(-1)
    return
if (f // 9 == 0):
    print(0)
else:
    print ("5" * (f - f % 9) + "0" * z)