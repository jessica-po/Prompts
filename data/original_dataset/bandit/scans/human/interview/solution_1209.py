from math import floor, ceil
n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
k = [floor(i) for i in arr]
delta = -sum(k)
for i in range(n):
    if int(arr[i]) != arr[i] and delta:
        delta -= 1
        print(ceil(arr[i]))
    else:
        print(floor(arr[i]))