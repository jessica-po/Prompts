import sys
n, a, b = list(map(int, input().split()))

cnt = 0
l = [set([x]) for x in range(1, n+1)]

while 1:
    l = list([tup[0] | tup[1] for tup in zip(l[::2], l[1::2])])
    cnt += 1
    for el in l:
        if a in el and b in el:
            print(cnt if len(el) < n else 'Final!')
            return