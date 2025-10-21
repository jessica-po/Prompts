l, r, k =list(map(int,input().split()))

d = {i:2**i for i in range(10)}

cache = {}

def can(i, m):
    return d[i] & m

def calc(m):
    b = 1
    c = 0
    for i in range(10):
        if b & m:
            c += 1
        b *= 2

    return c

def sm(ln, k, m, s='', first=False):
    if ln < 1:
        return 0, 1

    if (ln, k, m, s, first) in cache:
        return cache[(ln, k, m, s, first)]

    ans = 0
    count = 0
    base = 10 ** (ln-1)

    use_new = calc(m) < k

    if s:
        finish = int(s[0])+1
    else:
        finish = 10

    for i in range(finish):
        if use_new or can(i, m):
            ss = s[1:]
            if i != finish-1:
                ss = ''
            nm = m | d[i]
            nfirst = False
            if i == 0 and first:
                nm = m
                nfirst = True
            nexta, nextc = sm(ln-1, k, nm, ss, nfirst)
            ans += base * i * nextc + nexta
            count += nextc

#    print(ln, k, m, s, first, ans, count)
    cache[(ln, k, m, s, first)] = (ans, count)

    return ans, count

def call(a, k):
    s = str(a)
    return sm(len(s), k, 0, s, True)[0]


#print(call(r, k) - call(l-1, k))
print((call(r, k) - call(l-1, k)) % 998244353)