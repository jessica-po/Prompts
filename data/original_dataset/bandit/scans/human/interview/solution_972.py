def f():
    n, m = map(int, input().split())
    t = [input() for j in range(n)]

    p = [''.join(i) for i in zip(*t)]
    if h(p): return 1

    i = 0
    while i < n and not 'B' in t[i]: i += 1

    while i < n:
        a = t[i].find('B')
        if a < 0:
            i += 1
            break
        b = t[i].rfind('B')
        if 'W' in t[i][a: b + 1]: return 1

        for j in range(i + 1, n):
            if a > 0 and t[j][a - 1] == 'B' and t[j][b] == 'W': return 1
            if b < m - 1 and t[j][b + 1] == 'B' and t[j][a] == 'W': return 1
        i += 1

    while i < n:
        if 'B' in t[i]: return 1
        i += 1    

    return 0  
            
def h(t):
    i, n = 0, len(t)
    while i < n and not 'B' in t[i]: i += 1

    while i < n:
        a = t[i].find('B')
        if a < 0:
            i += 1
            break
        b = t[i].rfind('B')
        if 'W' in t[i][a: b + 1]: return 1
        i += 1

    while i < n:
        if 'B' in t[i]: return 1
        i += 1    

    return 0          
    
print('YNEOS'[f():: 2])