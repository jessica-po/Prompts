def main():
    n, m = list(map(int, input().split()))

    cost1 = []
    cost2 = []
    cost3 = []

    for i in range(n):
        w, c = list(map(int, input().split()))
        if w == 1:
            cost1.append(c)
        elif w == 2:
            cost2.append(c)
        else:
            cost3.append(c)

    cost1 = sorted(cost1)[::-1]
    cost2 = sorted(cost2)[::-1]
    cost3 = sorted(cost3)[::-1]
    cost3_prefix = [0]
    for c in cost3:
        cost3_prefix.append(cost3_prefix[-1] + c)


    dp = [(0, 0, 0)] * (m + 1)
    dp[0] = (0, 0, 0)

    for i in range(0, m):
        cost, n1, n2 = dp[i]

        if i + 1 <= m and n1 < len(cost1):
            new_cost = cost + cost1[n1]
            if dp[i + 1][0] < new_cost:
                dp[i + 1] = (new_cost, n1 + 1, n2)
        
        if i + 2 <= m and n2 < len(cost2):
            new_cost = cost + cost2[n2]
            if dp[i + 2][0] < new_cost:
                dp[i + 2] = (new_cost, n1, n2 + 1)

        if n1 == len(cost1) and n2 == len(cost2):
            break


    dp_prefix = [0]
    for x in dp[1:]:
        dp_prefix.append(max(dp_prefix[-1], x[0]))

    ans = 0
    for k in range(len(cost3) + 1):
        l = m - 3 * k
        if l < 0:
            continue

        new_ans = cost3_prefix[k] + dp_prefix[l]
        ans = max(new_ans, ans)

    print(ans)


def __starting_point():
    main()

__starting_point()