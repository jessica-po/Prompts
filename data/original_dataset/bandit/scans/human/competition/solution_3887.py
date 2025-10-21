#!/bin/python3

a = input()
while a:
    expr, n = a.split('=')
    n = int(n.strip())
    pos = 1
    neg = 0
    sg = [1]
    for c in expr:
        if c == '+':
            pos += 1
            sg.append(1)
        elif c == '-':
            neg += 1
            sg.append(0)
    csum = pos - neg
    rez = []
    for i in sg:
        if csum < n:
            if i > 0:
                v = min(n-csum, n-1)
                csum += v
                rez.append(1+v)
            else:
                rez.append(-1)
        else:
            if i > 0:
                rez.append(1)
            else:
                v = min(csum - n, n-1)
                csum -= v
                rez.append(-1-v)
    if csum == n:
        print("Possible")
        ans = str(rez[0])
        for j in rez[1:]:
            ans += " " + ("+" if j > 0 else "-") + " "
            ans += str(abs(j))
        ans += " = " + str(n)
        print(ans)
    else:
        print("Impossible")
    break
    a = input()