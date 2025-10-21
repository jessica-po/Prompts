g = {}
def push(u, v, w):
    g[u] = [v, w]
 
n, pos  = list(map(int, input().split()))
V = list(map(int, input().split()))
W = list(map(int, input().split()))
 
for _ in range(n):
    push(_, V[_], W[_])
 
max_log = 35
next_n  = [[-1] * n for _ in range(max_log)]
next_m  = [[float('inf')] * n for _ in range(max_log)]
next_s  = [[0] * n for _ in range(max_log)]
 
for u in range(n):
    v, w      = g[u]
    next_n[0][u]  = v
    next_m[0][u]  = w
    next_s[0][u]  = w
    
for k in range(1, max_log):
    for u in range(n):
        v  = next_n[k-1][u]
        m  = next_m[k-1][u]
        s  = next_s[k-1][u]
    
        next_n[k][u] = next_n[k-1][v] 
        next_m[k][u] = min(next_m[k-1][v], m)
        next_s[k][u] = next_s[k-1][v] + s
    
m_arr = [float('inf')] * n
s_arr = [0] * n
 
for _ in range(n):
    s, m = 0, float('inf')
    v    = _
    
    cur = 1<<max_log
    i   = max_log
 
    while cur > 0:
        if cur & pos:
            m = min(m, next_m[i][v])
            s = s + next_s[i][v]
            v = next_n[i][v]
            
        cur >>= 1
        i    -= 1
        
    m_arr[_] = m
    s_arr[_] = s
    
arr = [str(x) + ' ' + str(y) for x, y in zip(s_arr, m_arr)]
print('\n'.join([x for x in arr]))