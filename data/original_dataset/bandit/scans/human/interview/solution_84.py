from sys import stdin as cin
from sys import stdout as cout

def main():
    n = int(cin.readline())
    o = 0
    for x in range(9, 0, -1):
        if 10 ** x // 2 <= n:
            ##print(x)
            for i in range(9):
                q = 10 ** x * (i + 1) // 2 - 1
                if q <= n:
                    o += min(q, n - q)
            print(o)
            return
    print(n * (n - 1) // 2)

main()