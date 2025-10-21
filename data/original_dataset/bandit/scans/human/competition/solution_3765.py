import sys


MAXV = 100010
d = [0] * MAXV


a, b, h, w, n = list(map(int,input().split()))

arr = input().split()

for it in range(n):
    arr[it] = int(arr[it])

# print(arr)
# print(a, b, h, w, n)

def solve(a, b, h, w, z, product, it):
    # print(">", a, b, h, w, z, product, it)
    k = 0
    if a % h:
        k = a // h + 1
    else:
        k = a // h

    if k <= z and (product // z) * w >= b:
        print(it)
        return



arr = sorted(arr)
arr = arr[::-1]
# print(arr)

d[1] = 1
solve(a, b, h, w, 1, 1, 0)
solve(a, b, w, h, 1, 1, 0)
product = 1
xxx = 0

for it in range(1, n + 1):
    # arr[it - 1] = int(arr[it - 1])
    product *= arr[it - 1]
    # print("=", arr[it - 1])

    for j in reversed(list(range(1, MAXV))):
        if not d[j]:
            continue

        x = j * arr[it - 1]
        # x = min(x, MAXV - 1)
        if x < MAXV:
            d[x] = 1
        else:
            if xxx:
                xxx = min(x, xxx)
            else:
                xxx = x
    if xxx:
        solve(a, b, h, w, xxx, product, it)
        solve(a, b, w, h, xxx, product, it)

    for j in range(MAXV):
        if d[j]:
            solve(a, b, h, w, j, product, it)
            solve(a, b, w, h, j, product, it)


print(-1)