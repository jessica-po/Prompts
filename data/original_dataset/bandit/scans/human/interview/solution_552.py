import sys, logging
logging.basicConfig(level=logging.INFO)
logging.disable(logging.INFO)

def build(S, n):
    Z = [0 for i in range(3 * n + 3)]
    #logging.info(S)
    n = len(S)
    L = 0
    R = 0
    Z[0] = n
    for i in range(1, n):
        if(i > R):
            L = R = i
            while(R < n and S[R] == S[R - L]):
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if(Z[k] < R - i + 1):
                Z[i] = Z[k]
            else:
                L = i
                while(R < n and S[R] == S[R - L]):
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

def update1(n, x, val):
    while(x <= n + 1):
        bit1[x] += val
        x += x & -x

def get1(n, x):
    ans = 0
    while(x > 0):
        ans += bit1[x]
        x -= x & -x
    return ans

def update2(n, x, val):
    while(x <= n + 1):
        bit2[x] += val
        x += x & -x

def get2(n, x):
    ans = 0
    while(x > 0):
        ans += bit2[x]
        x -= x & -x
    return ans

def process(n, m, fa, fb):
    r2 = int(1)
    ans = 0
    for l1 in range(1, n + 1):
        while(r2 <= min(n, l1 + m - 2)):
            update1(n, m - fb[r2] + 1, 1)
            update2(n, m - fb[r2] + 1, fb[r2] - m + 1)
            r2 += 1
        ans += get1(n, fa[l1] + 1) * fa[l1] + get2(n, fa[l1] + 1)
        update1(n, m - fb[l1] + 1, -1)
        update2(n, m - fb[l1] + 1, m - 1 - fb[l1])
    print(ans)

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = sys.stdin.readline()
    b = sys.stdin.readline()
    s = sys.stdin.readline()
    a = a[:(len(a) - 1)]
    b = b[:(len(b) - 1)]
    s = s[:(len(s) - 1)]
    fa = build(s + a, n)
    kb = build(s[::-1] + b[::-1], n)
    fb = [0 for k in range(n + 2)]
    for i in range(m, m + n):
        fa[i - m + 1] = fa[i]
        if(fa[i - m + 1] >= m):
            fa[i - m + 1] = m - 1
        fb[m + n - i] = kb[i]
        if(fb[m + n - i] >= m):
            fb[m + n - i] = m - 1
    logging.info(fa[1:(n + 1)])
    logging.info(fb[1:(n + 1)])
    process(n, m, fa, fb)

bit1 = [0 for i in range(500004)]
bit2 = [0 for i in range(500004)]

def __starting_point():
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except:
        pass
    main()
__starting_point()