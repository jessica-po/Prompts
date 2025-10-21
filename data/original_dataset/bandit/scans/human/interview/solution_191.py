N, T = list(map(int, input().split()))
A = [int(a) for a in input().split()]
if sum(A) > N//2:
    A = [1-a for a in A][::-1]
K = sum(A)
S = sum(A[-K:])
M = K + 1
P = 10**9+7
inv = pow(N*(N-1)//2, P-2, P)
X = [[0]*M for _ in range(M)]
for i in range(M):
    if i > 0: X[i-1][i] = ((K-i+1)**2*inv)%P
    if i < M-1: X[i+1][i] = (N-2*K+i+1)*(i+1)*inv%P
    X[i][i] = (1-((K-i)**2*inv)-(N-2*K+i)*(i)*inv)%P

def ddd(n):
    for i in range(1, 100):
        if (n*i%P) < 100:
            return (n*i%P), i
    return -1, -1
def poww(MM, n):
    if n == 1:
        return MM
    if n % 2:
        return mult(poww(MM, n-1), MM)
    return poww(mult(MM,MM), n//2)
def mult(M1, M2):
    Y = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            for k in range(M):
                Y[i][j] += M1[i][k] * M2[k][j]
                Y[i][j] %= P
    return Y

X = poww(X, T)

print(X[S][K])