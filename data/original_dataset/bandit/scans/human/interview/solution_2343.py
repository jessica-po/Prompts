t = int(input())

def get_max(n):
    ans = 0
    while n:
        ans = 4 * ans + 1
        n = n - 1
        if ans > 10**19:
            break
    return ans

for _ in range(t):
    n, k = list(map(int, input().split()))
    if n == 1:
        if k == 1:
            print("YES 0")
        else:
            print("NO")
    elif n == 2:
        if k <= 2:
            print("YES 1")
        elif k != 3 and k <= 5:
            print("YES 0")
        else:
            print("NO")
    else:
        siz = n - 1
        l = 1
        cnt = 3
        while siz:
            if l <= k < l+cnt:
                print("YES {}".format(siz))
                break
            l = l + cnt
            cnt = 2 * cnt + 1
            siz = siz - 1
        else:
            if k <= get_max(n):
                print("YES 0")
            else:
                print("NO")