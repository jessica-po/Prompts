def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    colors = [[] for _ in range(k)]
    seen = [0 for _ in range(5003)]
    ans = [-1 for _ in range(n)]
    for i, x in enumerate(a):
        if seen[x] >= k:
            print('NO')
            return
        ans[i] = seen[x]
        colors[ans[i]].append(i)
        seen[x] += 1

    p = 0
    for i in range(k):
        if not colors[i]:
            while p < i and len(colors[p]) == 1:
                p += 1
            if p == i:
                print('NO')
                return

            colors[i].append(colors[p].pop())
            ans[colors[i][-1]] = i

    print('YES')
    print(' '.join(str(x + 1) for x in ans))

main()