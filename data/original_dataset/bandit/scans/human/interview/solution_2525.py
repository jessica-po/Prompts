S = input()
Q = int(input())
bs = ''
fs = ''
hanten = 0
for i in range(Q):
    query = list(input().split())
    if query[0] == '1':
        hanten += 1
    else:
        if query[1] == '1':
            if hanten % 2 == 0:
                fs += query[2]
            else:
                bs += query[2]
        else:
            if hanten % 2 == 0:
                bs += query[2]
            else:
                fs += query[2]
if hanten % 2 == 0:
    print(fs[::-1]+S+bs)
else:
    print(bs[::-1]+S[::-1]+fs)