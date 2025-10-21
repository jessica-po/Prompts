def main():
    X, Y, A, B, C = list(map(int, input().split()))
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    p.sort(reverse=True); q.sort(reverse=True); r.sort()

    p = p[:X]
    q = q[:Y]
    s = p + q
    s.sort()

    rtmp = r.pop()
    for i in range(len(s)):
        if s[i] < rtmp:
            s[i] = rtmp
            if len(r) == 0:
                break
            rtmp = r.pop()
        else:
            break
    ans = sum(s)
    print(ans)


def __starting_point():
    main()

__starting_point()