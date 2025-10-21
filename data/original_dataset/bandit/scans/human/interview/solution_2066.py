from collections import Counter
import string

def valid(o):
    for x, y in zip(o, o[1:]):
        if abs(ord(x) - ord(y)) == 1:
            return False

    return True

def create(c, o):
    res = []
    for x in o:
        for j in range(c[x]):
            res.append(x)
    return res

T = int(input())
for _ in range(T):
    c = Counter(input())
    o = []
    o1 = string.ascii_lowercase[1::2] + string.ascii_lowercase[::2]
    o2 = string.ascii_lowercase[::2] + string.ascii_lowercase[1::2]

    s1 = create(c, o1)
    s2 = create(c, o2)

    if valid(s1):
        print(''.join(s1))
    elif valid(s2):
        print(''.join(s2))
    else:
        print('No answer')