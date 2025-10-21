def ispalin(s):
    ans = True
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            ans = False
            break
        if i > len(s)//2:
            break
    return ans

for _ in range(int(input())):
    s = input()
    k = ''
    l = ''
    for j in range(len(s)):
        if s[j] == s[len(s)-1-j]:
            k += s[j]
            l = s[j] + l
        else:
            break
    if j != len(s)-1:
        t = ''
        y = ''
        for r in range(j,len(s)-j):
            t += s[r]
            if ispalin(t):
                y = t
        q = ''
        v = ''
        for r in range(len(s)-j-1,j-1,-1):
            q = s[r] + q
            if ispalin(q):
                v = q
        if len(v) > len(y):
            print(k+v+l)
        else:
            print(k+y+l)
    else:
        print(s)