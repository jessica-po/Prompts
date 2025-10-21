def solve():
    s = input()
    pm = 0
    cur = 0
    ans = len(s)
    for i in range(len(s)):
        if s[i] == '+':
            cur += 1
        else:
            cur -= 1
            if cur < pm:
                pm = cur
                ans += i + 1
    print(ans)
t = int(input())
for _ in range(t):
    solve()