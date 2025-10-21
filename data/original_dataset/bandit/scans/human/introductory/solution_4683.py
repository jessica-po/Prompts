(N), *D = [list(map(int, s.split())) for s in open(0)]
V = D[0]
A = V.pop(N[0]-1)
M = 1000000000 + 7
R=0
for value in reversed(V):
    R = R + ((A) * value) % M
    A = A + value
print(R % M)