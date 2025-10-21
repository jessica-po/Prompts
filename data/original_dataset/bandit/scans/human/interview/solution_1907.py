import sys

def inside(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) < (a[2]+b[2])**2


def main():
    pi = 3.14159265358979323
    n = int(sys.stdin.readline())
    a = []
    p = [-1]*n
    for i in range(n):
        x,y,r = map(int,sys.stdin.readline().split())
        a.append([x,y,r])

    for i in range(n):
        for j in range(n):
            if i==j :
                continue
            if inside(a[i],a[j]):
                if a[i][2] < a[j][2]:
                    if p[i] == -1:
                        p[i] = j
                    elif a[p[i]][2]>a[j][2]:
                        p[i] = j
                else:
                    if p[j] == -1:
                        p[j] = i
                    elif a[p[j]][2]>a[i][2]:
                        p[j] = i

    q = []
    for i in range(n):
        if p[i] == -1:
            q.append((i,True))

    s = len(q)
    ans = 0.0
    for i in range(s):
        c, b = q[i]
        for j in range(n):
            if p[j] == c:
                q.append((j,True))
        ans+= pi * a[c][2] * a[c][2]

    q = q[s:]
    while len(q)!=0 :
        c,b = q.pop()
        for j in range(n):
            if p[j] == c:
                q.append((j,not b))
        if b:
            ans+= pi * a[c][2] * a[c][2]
        else:
            ans-= pi * a[c][2] * a[c][2]

    print(ans)


main()