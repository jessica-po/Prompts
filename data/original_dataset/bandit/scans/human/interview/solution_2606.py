import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    t = sorted(map(int,input().split()))
    cur = [0]*(2*n)
    for i in range(n):
        low = high = t[i]
        while low and cur[low]:
            low -= 1
        while cur[high]:
            high += 1
        if low > 0 and i:
            lowsum = ind = j = 0
            cur[low] = 1
            while ind <= i:
                if cur[j]:
                    lowsum += abs(t[ind] - j)
                    ind += 1
                j += 1
            cur[low] = 0
            highsum = ind = j = 0
            cur[high] = 1
            while ind <= i:
                if cur[j]:
                    highsum += abs(t[ind] - j)
                    ind += 1
                j += 1
            cur[high] = 0
            if lowsum < highsum:
                cur[low] = 1
            else:
                cur[high] = 1
        else:
            cur[high] = 1
    ans = ind = j = 0
    while ind < n:
        if cur[j]:
            ans += abs(t[ind] - j)
            ind += 1
        j += 1
    print(ans)