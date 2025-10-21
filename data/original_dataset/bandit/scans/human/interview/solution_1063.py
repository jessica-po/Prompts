def solve(s, t, i, l):
    if i == l:
        return False
    if s[i] == "?":
        if solve(s, t, i + 1, l):
            s[i] = t[i]
            return True
        elif t[i] == "9":
            return False
        s[i] = nxt[t[i]]
        for j in range(i, l):
            if s[j] == "?":
                s[j] = "0"
        return True
    elif s[i] > t[i]:
        for j in range(i, l):
            if s[j] == "?":
                s[j] = "0"
        return True
    elif s[i] < t[i]:
        return False
    else:
        return solve(s, t, i + 1, l)


n = int(input())
a = [list(input()) for _ in range(n)]
p = ["0"]
nxt = {str(x): str(x + 1) for x in range(9)}

for i, ai in enumerate(a):
    if len(p) > len(ai):
        print("NO")
        break
    if len(p) < len(ai):
        if a[i][0] == "?":
            a[i][0] = "1"
        for j in range(len(ai)):
            if a[i][j] == "?":
                a[i][j] = "0"
    elif not solve(a[i], p, 0, len(ai)):
        print("NO")
        break
    p = a[i]
else:
    print("YES")
    print("\n".join("".join(line) for line in a))