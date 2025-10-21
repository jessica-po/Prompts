def main():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        t = input().strip()
        n = len(s)
        
        find = [[n] * 26 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            find[i][:] = find[i + 1]
            find[i][ord(s[i]) - ord("a")] = i

        def interleaving(a, b):
            dp = [n] * (len(b) + 1)
            for i in range(len(a) + 1):
                for j in range(len(b) + 1):
                    if i == j == 0:
                        dp[j] = -1
                        continue
                    res = n
                    if i > 0:
                        res = min(res, find[dp[j] + 1][ord(a[i - 1]) - ord("a")])
                    if j > 0:
                        res = min(res, find[dp[j - 1] + 1][ord(b[j - 1]) - ord("a")])
                    dp[j] = res
            return dp[-1] < n

        if any(interleaving(t[:i], t[i:]) for i in range(len(t))):
            print("YES")
        else:
            print("NO")


main()