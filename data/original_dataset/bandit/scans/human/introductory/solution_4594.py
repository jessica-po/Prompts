N = int(input())
ds = []
mochidan = 0
for i in range(N):
    ds.append(int(input()))

while ds:
    tmp = max(ds)
    ds = [j for j in ds if j < tmp]
    mochidan += 1

print(mochidan)