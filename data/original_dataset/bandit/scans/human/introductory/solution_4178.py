n = int(input())
hl = list(map(int, input().split()))
flg = True

hmax = hl[0]
for h in hl:
    hmax = max(hmax, h)
    if h >= hmax-1:
        continue
    else:
        flg = False

if flg:
    print('Yes')
else:
    print('No')