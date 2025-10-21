import sys

n = int(input())
c = list(map(int, input().split()))
cc = ord('a')
ans = ""
cur = n - 1
if 1:
    cur = n - 1
    while cur >= 0:
        while c[cur] > 0:
            if chr(cc) > 'z':
                cc = ord('a')
            ans += chr(cc) * (cur + 1)
            c[cur] -= 1
            for i in range(cur):
                c[i] -= (cur - i + 1)
            cc += 1
        cur -= 1
    print(ans)