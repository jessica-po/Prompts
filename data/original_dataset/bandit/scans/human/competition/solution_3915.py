def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]

ps = primes2(12*10**6)

def rub2(n):
    lst_odd = []
    lst_even = []
    for head in range(1, n):
        head_str = str(head)
        tail_str = head_str[::-1]
        lst_even.append(int(head_str + tail_str))
        lst_odd.append(int(head_str[:-1] + tail_str))
    lst = lst_odd + lst_even
    lst.sort()
    return lst

rs = rub2(12*10**2)

p, q = map(int, input().split())
idxp = len(ps) - 1
idxr = len(rs) - 1
pi = ps[idxp]
ri = rs[idxr]
while q * (idxp + 1) > p * (idxr + 1):
    if pi < ri:
        idxr -= 1
    elif pi > ri:
        idxp -= 1
    else:
        idxr -= 1
        idxp -= 1
    prev_pi = pi
    prev_ri = ri
    pi = ps[idxp]
    ri = rs[idxr]
print(max(prev_pi-1, prev_ri-1))