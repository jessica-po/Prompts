def s(arr):
    arr2 = arr[:]
    arr2.sort()
    return arr == arr2

x = int(input())
y = list(map(int, input().split(' ')))
while (not s(y)):
    for i in range(x-1):
        if y[i] > y[i+1]:
            print(i+1, i+2)
            y[i], y[i+1] = y[i+1], y[i]