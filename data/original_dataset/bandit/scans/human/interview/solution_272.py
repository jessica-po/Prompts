a = input()
b = input()

symbols = {}
pairs = []

for i in range(len(a)):
    if a[i] in symbols:
        if symbols[a[i]] != b[i]:
            print('-1')
            break
    elif b[i] in symbols:
        if symbols[b[i]] != a[i]:
            print('-1')
            break
    else:
        symbols[a[i]] = b[i]
        symbols[b[i]] = a[i]
        if a[i] != b[i]:
            pairs.append((a[i], b[i]))
else:
    print(len(pairs))
    for elem in pairs:
        print(elem[0], elem[1])