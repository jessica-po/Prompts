def main():
    N = int(input())
    S = list(map(int, input().split()))
    INF = float('inf')

    S.sort()

    parents = [S[-1]]
    S[-1] = INF

    for _ in range(N):
        checking = 2
        parents.sort(reverse=True)
        for i in parents[:]:
            while True:
                if S[-checking] < i:
                    parents.append(S[-checking])
                    S[-checking] = INF
                    break
                else:
                    checking += 1
                if checking == 2 ** N + 1:
                    print('No')
                    return
    else:
        print('Yes')


def __starting_point():
    main()
__starting_point()