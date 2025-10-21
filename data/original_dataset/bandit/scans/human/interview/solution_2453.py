3

def solve(N, A):
    cnt = [0] * (N + 1)

    evd = {}
    xs = []
    for a, b in A:
        if a not in evd:
            evd[a] = [0, 0]
            xs.append(a)
        if b not in evd:
            evd[b] = [0, 0]
            xs.append(b)

        evd[a][0] += 1
        evd[b][1] += 1

    xs.sort()

    px = xs[0] - 1
    pop = 0
    for x in xs:
        cnt[pop] += x - px - 1
        cnt[pop + evd[x][0]] += 1
        pop -= evd[x][1]
        pop += evd[x][0]
        px = x

    return cnt[1:]


def main():
    N = int(input())
    A = [tuple([int(e) for e in input().split(' ')]) for _ in range(N)]
    print(*solve(N, A))


def __starting_point():
    main()

__starting_point()