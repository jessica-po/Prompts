#!/usr/bin/env python3
n = int(input())
arr = []

for i in range(n):
    arr.append(1)
    while len(arr)>=2 and arr[-1] == arr[-2]:
        a, b = arr.pop(), arr.pop()
        arr.append(a+1)

print(' '.join(map(str, arr)))