n = int(input())
d = dict()
for i in range(n):
    d[input()] = i

lst = list(d.items())

lst.sort(key=lambda x:-x[1])

for i in lst:
    print(i[0])