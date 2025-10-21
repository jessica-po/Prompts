from scipy.special import comb
mod = 10**9 + 7
N, K = list(map(int,input().split()))
for i in range(1,K+1):
    a = K-i
    b = i-1
    c = N-(i-1)-K
    d = i
    print((comb(a+b,b,exact=True)*comb(c+d,d,exact=True)%mod))