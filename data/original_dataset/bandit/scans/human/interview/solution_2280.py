t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    print(min(arr[1] - 1, len(arr) - 2))