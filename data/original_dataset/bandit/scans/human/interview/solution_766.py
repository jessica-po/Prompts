s = input()
ss = set(s)

if len(s) >= 4:
    if len(ss) in (3, 4):
        print('Yes')
    elif len(ss) == 2:
        for c in ss:
            if s.count(c) == 1:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')
else:
    print('No')