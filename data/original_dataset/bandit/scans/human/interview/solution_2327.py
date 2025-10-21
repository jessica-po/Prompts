import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    ans = 0
    f = 0
    i = n
    while n:
        ans += i // 2**f
        n //= 2
        f += 1
    print(ans)