def solve():
    n = int(input())
    A = list(map(int, input().split()))
    x, A = A[0], A[1:]
    A = [(A[i], i + 2) for i in range(len(A))]
    A.sort(reverse=True)

    cnt = 1
    msg = x
    total = 1
    for a in A:
        if not msg:
            print(-1)
            return
        msg += a[0] - 1
        total += a[0]
        cnt += 1
        if total >= n:
            break

    print(n - 1)
    total = x
    for j in range(min(x, len(A))):
        print(1, A[j][1])
    if total >= n - 1:
        return
    for i in range(len(A)):
        for j in range(total, min(total + A[i][0], len(A))):
            print(A[i][1], A[j][1])
            total += 1
            if total >= n - 1:
                return


solve()