s = input()
last = s.rfind('#')
dif = s.count('(')-s.count(')')-s.count('#')
try:
    assert dif >= 0
    lev = 0
    out = []
    for i in range(len(s)):
        c = s[i]
        if c == '(': lev += 1
        elif c == ')':
            lev -= 1
            assert lev >= 0
        elif c == '#':
            lev -= 1
            if i == last:
                out.append(dif+1)
                lev -= dif
            else:
                out.append(1)
            assert lev >= 0
    assert lev == 0
    for x in out: print(x)
except AssertionError:
    print(-1)