for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input().strip()
    ans = (n + 1) * b + n * a
    
    if '1' in s:
        ans += 2 * a
        s = s[s.find('1'):s.rfind('1') + 1]
        t = [0] * (len(s) + 1)
        for i in range(len(s)):
            x = int(s[i])
            t[i] = max(t[i], x)
            t[i + 1] = max(t[i + 1], x)
        i = 0
        while i < len(t):
            j = i + 1
            while j < len(t) and t[i] == t[j]:
                j += 1
            if t[i]:
                ans += b * (j - i)
            else:
                ans += min(b * (j - i), 2 * a) 
            i = j
    
    print(ans)