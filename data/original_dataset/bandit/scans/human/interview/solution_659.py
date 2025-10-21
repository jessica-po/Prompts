import sys

def solve():
    n, = rv()
    a, = rl(1)
    for i in range(min(10, n - 1)):
        for j in range(max(i + 1, n - 10), n):
            if a[i] != a[j]:
                a[i], a[j] = a[j], a[i]
                if notsorted(a):
                    print(i + 1, j + 1)
                    return
                a[i], a[j] = a[j], a[i]
    count = 0
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            if notsorted(a):
                print(i + 1, i + 2)
                return
            a[i], a[i + 1] = a[i + 1], a[i]
            count += 1
        if count == 100: break
    print(-1)

def notsorted(a):
    first, second = True, True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            first = False
            break
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            second = False
            break
    return True if not first and not second else False



def prt(l): return print(''.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()