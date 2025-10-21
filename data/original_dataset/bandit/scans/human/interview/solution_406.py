arr = [0] * (10 ** 6 + 1)
n = int(input())
for i in input().split():
    arr[int(i)] += 1
i = 10 ** 6
j = i
k = i
c = 0
while j > 0:
    if arr[j] % 2 == 1 and (arr[j] > 1 or c == 0):
        arr[j - 1] += 1
        c = 1
    else:
        c = 0
    j -= 1
r = 0
while i > 0 and k > 0:
    if arr[i] < 2:
        if i == k:
            k -= 1
        i -= 1
    elif i == k and arr[i] < 4:
        k -= 1
    elif arr[k] < 2:
        k -= 1
    else:
        r += i * k
        arr[i] -= 2
        arr[k] -= 2
print(r)