from collections import defaultdict
def main():
    n, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    s = []
    ord = [-1]*(n+1)
    u = 1
    while ord[u] == -1:
        ord[u] = len(s)
        s.append(u)
        u = a[u-1]
    l = len(s) - ord[u]
    if k < ord[u]:
        print(s[k])
    else:
        print(s[(k-ord[u])%l+ord[u]])

'''
def main():
    n, k = map(int, input().split(" "))
    a = list(map(lambda i: int(i)-1, input().split(" ")))
    s = [0]
    d = defaultdict(lambda:0)
    x = a[0]
    for i in range(n):
        s.append(x)
        x = a[x]

    bb=None
    for i in range(n):
        d[s[i]] += 1
        if d[s[i]] ==2:
            bb=s[i]
            break

    cc = s.index(bb)
    s[cc]=-1
    dd = s.index(bb)
    loop_len = dd-cc
    s[cc]=s[dd]
        
    if bb ==None or k < cc:
        print(s[k]+1)
    else:
        y = (k-cc) % loop_len
        print(s[y+cc]+1)
'''
def __starting_point():
    main()
__starting_point()