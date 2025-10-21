n,k,a,b = map(int,input().split())
A = []
per = 0
if a >= b:
    per=0
    while True:
        if b == 0:
            if a <=k:
                A.append('G'*a)
                break
            else:
                per = 1
                break
        else:
            if a-b>=k-1:
                a-=k
                b-=1
                A.append('G'*k + 'B')
            elif a - b > 0:
                A.append((a-b+1) * 'G' + 'B')
                a -= (a-b+1)
                b -= 1
            else:
                A.append('GB' * a)
                break
else:
    a,b=b,a
    per=0
    while True:
        if b == 0:
            if a <=k:
                A.append('B'*a)
                break
            else:
                per = 1
                break
        else:
            if a-b>=k-1:
                a-=k
                b-=1
                A.append('B'*k + 'G')
            elif a - b > 0:
                A.append((a-b+1) * 'B' + 'G')
                a -= (a-b+1)
                b -= 1
            else:
                A.append('BG' * a)
                break
if per == 1:
    print('NO')
else:
    print(''.join(map(str,A)))