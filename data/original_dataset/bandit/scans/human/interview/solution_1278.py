n, x, y = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
for i in range(n):
    if arr[i] == min(arr[max(0, i - x):i + y + 1]):
        print(i + 1)
        break