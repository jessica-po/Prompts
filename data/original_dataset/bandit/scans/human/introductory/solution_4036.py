"""

b[i] = a[i] - i - 1

b[i] <= b[i+1] < 2b[i] + i - 1

sum(b) == r
"""

def solve(n, k):

    r = n - k*(k+1)//2
    if r < 0:
        return None

    b0 = r//k

    r -= b0*k

    seq = [None]*k
    seq[0] = b0
    b = b0

    for i in range(1,k):
        bn = b*2 + i - 1

        h = r//(k-i)
        if h > 0:
            if h+b > bn:
                h = bn - b
            r -= h*(k-i)
            b = h+b
        seq[i] = b
    if r != 0:
        return None
    A = [b+i+1 for i,b in enumerate(seq)]
    return A


def main():
    n,k = map(int,input().split())
    res = solve(n,k)
    if res is None:
        print('NO')
    else:
        print('YES')
        print(*res)
main()