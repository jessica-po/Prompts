n, w, v, u = list(map(int, input().split()))
versh = []
for i in range(n):
    a, b = list(map(int, input().split()))
    versh.append((a, b))
versh.sort(key=lambda x : x[1])
for i in versh:
    if i[0] / v < i[1] / u:
        break
else:
    print(w / u)
    return
y = 0
time = 0
for i in versh:
    x = i[0] - time * v
    if x < 0:
        continue
    if x / v >= (i[1] - y) / u:
        time += x / v
        y = i[1]
time += (w - y) / u
print(time)