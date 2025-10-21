n, m = input().split()
n = int(n)
m = int(m)
a = []
N = n
for i in range(n) :
    a.append(input().split())
    
for i in range(n) :
    if a[i][0].find('*') == -1 :
        n-=1
    else :
        break
if n != 1 :
    for i in range(len(a)-1,-1,-1) :
        if a[i][0].find('*') == -1 :
            n-=1
        else :
            break
#print(n)

M = m
br = 0
for i in range(m) :
    count = 0
    for j in range(len(a)) :
        if a[j][0][i] != ('*') :
            count+=1
        else :
            br = 1
            break
    if br == 1 :
        break
    if count == N :
        m-=1
br = 0
if m != 1 :
    for i in range(M-1,-1,-1) :
        count = 0
        for j in range(len(a)) :
            if a[j][0][i] != ('*') :
                count+=1
            else :
                br = 1
                break
        if br == 1 :
            break
        if count == N :
            m-=1
#print(m)
if m > n :
    print(m)
else :
    print(n)