n = int(input())
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
m = n+1
if n == 1:
    print(0)
else:
    for a in range(-1, 2):
        for b in range(-1, 2):
            c = True
            p = (T[1]+b) - (T[0]+a)
            tot = 0
            if a!=0:
                tot+=1
            if b!=0:
                tot+=1
            el = T[1]+b
            for j in range(2, n):
                if abs((T[j] - el) - p) <= 1:
                    el += p
                    if T[j] != el:
                        tot+=1
                else:
                    c = False
            if c:
                m = min(m, tot)
    if m <= n:
        print(m)
    else:
        print(-1)