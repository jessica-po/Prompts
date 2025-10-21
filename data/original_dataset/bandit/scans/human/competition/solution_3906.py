N, M = list(map(int, input().split()))
P = 10**9+7
F = [1, 2]
for i in range(101010):
    F.append((F[-1]+F[-2])%P)
print((F[N-1]+F[M-1]-1)*2%P)