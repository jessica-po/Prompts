for __ in range(int(input())):
    a = list(map(int, input()))
    ar1 = []
    ar2 = []
    for elem in a:
        if elem % 2 == 0:
            ar1.append(elem)
        else:
            ar2.append(elem)
    ans = []
    i = 0
    j = 0
    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            ans.append(ar1[i])
            i += 1
        else:
            ans.append(ar2[j])
            j += 1
    if i < len(ar1):
        for h in range(i, len(ar1)):
            ans.append(ar1[h])
    if j < len(ar2):
        for h in range(j, len(ar2)):
            ans.append(ar2[h])
    print(''.join(map(str, ans)))