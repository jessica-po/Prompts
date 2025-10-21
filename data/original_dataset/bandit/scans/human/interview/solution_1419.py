import sys

inf = 1 << 30

def solve():
    def check(mid):
        tot = 1
        line = 0
        buf = 0

        for ch in s:
            buf += 1

            if ch == ' ' or ch == '-':
                if line + buf > mid:
                    tot += 1

                    if tot > k or buf > mid:
                        return False

                    line = buf
                    buf = 0
                else:
                    line += buf
                    buf = 0

        if line + buf > mid:
            tot += 1

            if tot > k or buf > mid:
                return False

        return True

    k = int(input())
    s = input()

    # binary-search
    top = len(s)
    btm = 0

    while top - btm > 1:
        mid = (top + btm) // 2

        if check(mid):
            top = mid
        else:
            btm = mid

    ans = top

    print(ans)

def __starting_point():
    solve()
__starting_point()