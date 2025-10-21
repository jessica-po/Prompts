n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
arr2 = []
for i in range(n):
    arr2.append((arr[i], i))
arr2.sort()
ans = []
for i in arr2:
    if k >= i[0]:
        k -= i[0]
        ans.append(i[1])
print(len(ans))
for i in ans:
    print(i + 1, end = ' ')