n, k, p = [int(c) for c in input().split()]
a = [int(c) for c in input().split()]

nech= []
ch = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        ch.append(a[i])
    else:
        nech.append(a[i])

needed_nech = k - p

free_nech = len(nech) - needed_nech
av_ch = len(ch) + (free_nech // 2)

sets = []


if free_nech < 0 or free_nech % 2 != 0 or av_ch < p:
    print('NO')
else:
    print('YES')
    while needed_nech > 0:
        sets.append([nech.pop()])
        needed_nech -= 1

    while p > 0:
        if len(ch) > 0:
            sets.append([ch.pop()])
        else:
            sets.append([nech.pop(), nech.pop()])
        p -= 1

    sets[0] = sets[0] + nech + ch

for i in range(len(sets)):
    print(len(sets[i]),' '.join(map(str,sets[i])))