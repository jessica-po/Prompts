n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def try_solve(t):
    for i in range(n-1):
        ok = False

        for x in range(4):
            if a[i] == t[i] | x and b[i] == t[i] & x:
                t.append(x)
                ok = True
                break

        if not ok:
            return False

    return True

ok = False

for x in range(4):
    t = [x]

    if try_solve(t):
        print("YES")
        print(" ".join(map(str, t)))
        ok = True
        break

if not ok:
    print("NO")