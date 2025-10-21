def read_line():
    return list(map(int, input().split()))
def pr(l):
    a = 1
    for x in l:
        a *= x
    return a

T = int(input())
for _ in range(T):
    n = int(input())
    l = list(sorted(read_line()))
    l2 = list(reversed(l))
    m = None
    for i in range(6):
        j = 5 - i
        a = l[:i]
        b = l2[:j]
        p = pr(a) * pr(b)
        if m == None or p > m:
            m = p
    print(m)