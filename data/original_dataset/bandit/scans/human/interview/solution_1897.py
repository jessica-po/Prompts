arr = []
for i in input():
    arr.append(i)
n = len(arr)
res = 0
add = [0] * (n + 10)
add[n] = 1 / n
for i in range(n - 1, 0, -1):
    add[i] = add[i + 1] + 1 / i
for i in range(n):
    if arr[i] in ['I', 'E', 'A', 'O', 'U', 'Y']:
        x = min(i, n - i - 1)
        y = max(i, n - i - 1)
        res += x + 1
        res += (x + 1) * (add[x + 2] - add[y + 1])
        res += (n + 1) * add[y + 1] - (n - y)
print(res)