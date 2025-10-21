mod = int(1e9 + 7)
n, m = map(int, input().split())
f = [ [0 for i in range(60)] for j in range(60) ]
g = [ [0 for i in range(60)] for j in range(60) ]
s = [ [0 for i in range(60)] for j in range(60) ]
inv = [ 1 ]
f[0][0] = s[0][0] = 1

def pow(x, exp) :
    res = 1
    for i in range(0, 31) :
        if exp & 1 : res = res * x % mod
        exp >>= 1
        if exp == 0 : break
        x = x * x % mod
    return res

for i in range(1, n + 1) :
    inv.append( pow(i, mod - 2) )

for node in range(1, n + 1) :
    for cut in range(1, n + 1) :
        tmp = 0
        for ln in range(node) :
            for lc in range(cut - 1, n + 1) :
                if f[ln][lc] == 0 : continue
                if lc == cut - 1 :
                    tmp = ( tmp + f[ln][lc] * s[node - ln - 1][cut - 1] ) % mod
                else :
                    tmp = ( tmp + f[ln][lc] * f[node - ln - 1][cut - 1] ) % mod
        cnt = 1
        if tmp != 0 :
            cn, cc = 0, 0
            for i in range(1, n + 1) :
                cn += node
                cc += cut
                cnt = cnt * (tmp + i - 1) % mod * inv[i] % mod
                if cn > n or cc > n : break
                for j in range(n - cn, -1, -1) :
                    for k in range(n - cc, -1, -1) :
                        if f[j][k] == 0 : continue
                        g[j + cn][k + cc] += f[j][k] * cnt
                        g[j + cn][k + cc] %= mod
            for i in range(n + 1) :
                for j in range(n + 1) :
                    f[i][j] = (f[i][j] + g[i][j]) % mod
                    g[i][j] = 0
            
    for cut in range(n, -1, -1) :
        s[node][cut] = ( s[node][cut + 1] + f[node][cut] ) % mod
print(f[n][m - 1])