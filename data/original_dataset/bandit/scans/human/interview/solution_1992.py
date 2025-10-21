n, m, k = map(int, input().split())
arr = [0] * n
pl = [0] * n
z = 0
for i in input().split():
    j = int(i)
    arr[j - 1] = z
    pl[z] = j - 1
    z += 1
#print(arr, pl)
r = 0
for i in input().split():
    j = int(i) - 1
    c = arr[j]
    r += c // k + 1
    if c != 0:
        pl[c - 1], pl[c] = pl[c], pl[c - 1]
        arr[pl[c]] += 1
        arr[j] -= 1
    #print(arr, pl)
print(r)