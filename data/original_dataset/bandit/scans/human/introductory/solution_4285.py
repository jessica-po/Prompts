def num(s):
    ans1 = [0]*n
    for q in range(n):
        ans1[q] = s[q] == 'a'
    sum1 = 0
    for q in range(n):
        w = sum1*(s[q] == 'b')
        sum1 += ans1[q]
        ans1[q] = w
    sum1 = 0
    for q in range(n):
        w = sum1*(s[q] == 'c')
        sum1 += ans1[q]
        ans1[q] = w
    sum1 = 0
    for q in range(n):
        sum1 += ans1[q]
    return sum1 % C


n = int(input())
s = list(input())
C, k = 10**9+7, 0
ans, ans1, deg = [0]*n, [0]*n, [1]
for q in range(n):
    deg.append(deg[-1]*3 % C)
    k += s[q] == '?'
if k == 0:
    print(num(s))
elif k == 1:
    ans = 0
    for q in range(n):
        if s[q] == '?':
            for q1 in ['a', 'b', 'c']:
                s[q] = q1
                ans += num(s)
            break
    print(ans % C)
elif k == 2:
    ans = 0
    ind1 = ind2 = -1
    for q in range(n):
        if s[q] == '?' and ind1 == -1:
            ind1 = q
        elif s[q] == '?':
            ind2 = q
    for q in ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']:
        s[ind1], s[ind2] = q[0], q[1]
        ans += num(s)
    print(ans % C)
else:
    ans = 0
    for q1 in ['???', '??c', '?b?', '?bc', 'a??', 'a?c', 'ab?', 'abc']:
        t = q1.count('?')
        ans1 = [0] * n
        for q in range(n):
            ans1[q] = (s[q] == q1[0])*deg[k-t]
        sum1 = 0
        for q in range(n):
            w = sum1 * (s[q] == q1[1])
            sum1 += ans1[q]
            ans1[q] = w % C
        sum1 = 0
        for q in range(n):
            w = sum1 * (s[q] == q1[2])
            sum1 += ans1[q]
            ans1[q] = w % C
        sum1 = 0
        for q in range(n):
            sum1 += ans1[q]
        ans += sum1
    print(ans % C)