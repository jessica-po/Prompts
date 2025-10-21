# You lost the game.
n, m = map(int, input().split())
A = list(map(int, input().split()))
M = [list(map(int, input().split())) for _ in range(m)]

j = m-1
x = 2
h = -1
B = [-1 for _ in range(n+1)]
while h < n and j >= 0:
    h = M[j][1]
    if h >= x:
        B[h] = j
        x = h+1
    j -= 1

O = [0 for _ in range(n)]

for i in range(n-1,x-2,-1):
    O[i] = A[i]
    del A[i]

n2 = len(A)
    
R = A[:]
R.sort()
      
d = 0
f = n2-1


c = 0
for i in range(n2-1,-1,-1):
    j = B[i+1]
    if j >= 0:
        c = M[j][0]
    if c == 1:
        O[i] = R[f]
        f -= 1
    else:
        O[i] = R[d]
        d += 1

    
for i in range(n):
    print(O[i],end=" ")