n , k = input().split()

n , k = int(n), int(k)

d = {}

arr = list(map(int, input().split()))
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1;

arr = list(set(arr))
arr.sort()

cnt = 0
for i in range(len(arr)-1):
    if (arr[i] + k >= arr[i+1]):
        cnt += d[arr[i]]

print(n - cnt)