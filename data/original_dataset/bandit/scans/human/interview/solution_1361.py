def calcdiff(listx):
    maxim = -1
    for i in range(1, len(listx)):
        maxim = max(maxim, listx[i] - listx[i-1])
    return maxim
x = int(input())
t = list(map(int, input().split(' ')))
maximx = 90000001
for i in range(1, x-1):
    maximx = min(maximx, calcdiff(t[:i] + t[i+1:]))
print(maximx)