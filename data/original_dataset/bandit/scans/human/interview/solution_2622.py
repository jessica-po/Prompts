n, m = [int(x) for x in input().split()]
list1 = []
list2 = []
for i in range(n):
    list1.append(input())

for j in range(m):
    list2.append(input())

list3 = []
for i in range(n - m + 1):
    y = ""
    for j in range(m):
        y += list1[j + i]
    list3.append(y)

list4 = []
for i in range(n - m + 1):
    y = ""
    for j in range(m):
        y += list2[j][i:i + m]
    list4.append(y)

for i in list3:
    if i in list4:
        print(list3.index(i) + 1, list4.index(i) + 1)
        quit()