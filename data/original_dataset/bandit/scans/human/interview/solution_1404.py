MOD = 998244353.0
float_prec = 1801439850948198.4
float_mod = lambda x: x if -float_prec < x < float_prec else x % MOD

n = int(input())
a = [int(i) for i in input().split()]

f0, f1 = [1.0] * 201, [0.0] * 201
for i in range(n):
    nf0, nf1 = [0.0] * 201, [0.0] * 201
    if a[i] == -1:
        for j in range(200):
            nf0[j + 1] = float_mod(nf0[j] + f0[j] + f1[j])
            nf1[j + 1] = float_mod(nf1[j] - f0[j] + f0[j + 1] - f1[j] + f1[200])
    else:
        for j in range(200):
            nf0[j + 1], nf1[j + 1] = nf0[j], nf1[j]
            if j + 1 == a[i]:
                nf0[j + 1] = float_mod(nf0[j] + f0[j] + f1[j])
                nf1[j + 1] = float_mod(nf1[j] - f0[j] + f0[j + 1] - f1[j] + f1[200])
    f0, f1 = nf0, nf1

print(int(f1[200] % MOD))