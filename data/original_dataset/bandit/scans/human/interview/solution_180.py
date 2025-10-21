s = input()
k = int(input())
c = 0
p = 0
has_star = False
for i in range(len(s)):
    if s[i] in ['*', '?']:
        if s[i] == '*':
            has_star = True
        c -= 1
    else:
        p += 1
        c += 1
if k < c:
    print("Impossible")
elif (not has_star) and (k > p):
    print("Impossible")
else:
    signs_to_add = k - c
    ans = ""
    for i in s:
        if signs_to_add == 0:
            if i not in ['*', '?']:
                ans += i
            else:
                ans = ans[:-1]
            continue
        if i == '?':
            signs_to_add -= 1
        elif i == '*':
            signs_to_add -= 1
            while signs_to_add > 0:
                ans += ans[-1]
                signs_to_add -= 1
        else:
            ans += i
    print(ans)