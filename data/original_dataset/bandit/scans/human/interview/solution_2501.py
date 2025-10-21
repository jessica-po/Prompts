from collections import defaultdict

def main():
    d = defaultdict(int)
    d2 = defaultdict(int)

    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        d[i + 1 + A[i]] += 1
        d2[max(0, (i + 1) - A[i])] += 1

    ans = 0

    for k,v in d.items():
        if k == 0:continue
        ans += v * d2[k]

    print(ans)

def __starting_point():
    main()
__starting_point()