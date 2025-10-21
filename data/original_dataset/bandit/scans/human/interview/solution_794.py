n = int(input().strip())
arr = list(map(int, input().strip().split()))
if len(set(arr)) == 1:
    print(-1);return()
arr.sort()
print(*arr)