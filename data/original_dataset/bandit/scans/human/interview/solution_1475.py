p = 10 ** 9 + 7
n, b, k, x = [int(s) for s in input().split()]
block = [int(s) for s in input().split()]
D = [0 for i in range(10)]
for s in block:
    D[s] += 1
A = [[0 for t in range(x)]]
pows = [pow(10, 1<<j, x) for j in range(b.bit_length())]
for i in range(10):
    A[0][i%x] += D[i]
for j in range(b.bit_length()-1):
    B = A[-1]
    C = [sum(B[i]*B[(t - i*pows[j])%x] for i in range(x)) % p for t in range(x)]
    A.append(C)
ans = None
for j in range(b.bit_length()):
    if (b>>j)&1:
        if ans is None:
            ans = A[j][:]
        else:
            ans = [sum(A[j][(t - i*pows[j])%x]*ans[i] for i in range(x)) % p for t in range(x)]
print(ans[k])