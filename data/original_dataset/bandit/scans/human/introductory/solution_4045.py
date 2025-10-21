n = int(input())
s = input()
t = input()
#n = 1
#s2 = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
us = ["abc", "acb", "bac", "bca", "cab", "cba"]
flag = 0
for u in us:
    if (s in u or t in u):
        continue
    if (n > 1 and (s in (u[2] + u[0]) or t in (u[2] + u[0]))):
        continue
    flag = 1
    print("YES")
    print(u * n)
    return

if (not flag):
    for u in us:
        if (s in u or t in u):
            continue
        print("YES")
        print(u[0] * n + u[1] * n + u[2] * n)
        return