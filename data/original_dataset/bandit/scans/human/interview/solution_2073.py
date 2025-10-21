# You lost the game.
n = int(input())
A = list(map(int, input().split()))

V = [0 for _ in range(n)]
G = V[:]

def visiter(i,d):
    nonlocal V
    nonlocal G
    G[i] = d+1
    V[i] = d+1
    c = d+2
    while 1:
        if V[A[i]-1] and G[A[i]-1] > d:
            return 1,c-G[A[i]-1],G[A[i]-1]-1-d,c
        elif V[A[i]-1]:
            return 0,0,c-1-d,c
        else: 
            G[A[i]-1] = c
            c += 1
            V[A[i]-1] = 1
            i = A[i]-1



T = [1 for _ in range(n+1)]
for i in range(1,n+1):
    T[i] = (T[i-1]*2) % (10**9 + 7)

R = []
d = 0
i = 0
c = 0
for i in range(n):
    if V[i] == 0:
        v,l,s,c = visiter(i,c)
        if v:
            R += [l]
        d += s
        
r = T[d]
for x in R:
    r = (r*(T[x]-2)) % (10**9 + 7)
print(r)