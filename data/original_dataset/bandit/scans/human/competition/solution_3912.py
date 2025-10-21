#!/usr/bin/env python3

def main():
    import collections

    n = int(input())
    s = input()
    alph = collections.Counter(s)
    odd = sum(x & 0x1 for x in alph.values())
    dq = collections.deque()
    if odd == 0:
        print(1)
        for c, x in alph.items():
            dq.append(c * (x >> 1))
            dq.appendleft(c * (x >> 1))
        print(*dq, sep="")
    else:
        for odd in range(odd, n):
            if (n - odd) % (odd << 1) == 0:
                print(odd)
                odds = [c for c, x in alph.items() if x & 0x1]
                items = list(alph.items())
                while len(odds) != odd:
                    for i, x in enumerate(items):
                        if x[1] > 1:
                            items[i] = (x[0], x[1] - 2)
                            odds.append(x[0])
                            odds.append(x[0])
                            break
                req_length = (n - odd) // odd + 1
                cur_length = 0
                while odd > 0:
                    if cur_length == 0:
                        dq.append(odds[-1])
                        cur_length += 1
                        odds.pop()
                    x = min(items[-1][1] >> 1, (req_length - cur_length) >> 1)
                    dq.append(items[-1][0] * x)
                    dq.appendleft(items[-1][0] * x)
                    cur_length += x << 1
                    if items[-1][1] - (x << 1) <= 1:
                        items.pop()
                    else:
                        items[-1] = (items[-1][0], items[-1][1] - (x << 1))
                    if cur_length == req_length:
                        print(*dq, sep="", end=' ')
                        odd -= 1
                        dq.clear()
                        cur_length = 0
                print()
                break
        else:
            print(n)
            print(*s)

try:
    while True:
        main()
except EOFError:
    pass