n = int(input())
a = input()
kol1 = 0
kol0 = 0
for i in range(len(a)):
    if a[i] == "1":
        kol1 += 1
    else:
        kol0 += 1
print(abs(kol1 - kol0))