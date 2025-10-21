N, M, X = list(map(int, input().split()))
A = [0]*N

for i in range(N):
    A[i] = list(map(int, input().split()))

min_sump = -1
for i in range(2**(N+1)):
    sump = 0
    sume = [0]*M
    for j in range(N):
        ns = "0" + str(N) +"b"
        bi = format(i,ns)
        if bi[-1-j] == "1":
            sump += A[j][0]
            sume = list(map(sum, zip(sume, A[j][1:])))
    if all([i >= X for i in sume]):
        if min_sump == -1:
            min_sump = sump
        else:
            min_sump = min(min_sump,sump)

print(min_sump)