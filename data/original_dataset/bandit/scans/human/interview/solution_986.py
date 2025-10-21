n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
library = []
money = 0
for i in range(len(a)):
    if a[i] not in library:
        money += 1
        if len(library) < k:
            library.append(a[i])
        else:
            curmin = n
            curindex = 0
            found = [n] * len(library)
            for j in range(len(a[i+1::])):
                if (a[i+j+1] in library) and (found[library.index(a[i+j+1])]==n):
                    found[library.index(a[i+j+1])] = j
            library[found.index(max(found))] = a[i]
print(money)