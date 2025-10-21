import sys

MOD = 10**9+7

# Polymod
def polymod(P,Q):
    assert(Q[-1]==1)
    n = len(Q)
    while len(P)>=n:
        p = P[-1]
        for i in range(n):
            P[-i-1] -= p*Q[-i-1]
        assert(P[-1]==0)
        P.pop()
    return P

def polyprod(P,Q):
    n = len(P)
    m = len(Q)
    W = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            W[i+j]+=P[i]*Q[j]
    return [w%MOD for w in W]

# Calc A^m * B 
def power(A,B,m,mult):
    if m == 0:
        return B
    while m>1:
        if m%2==1:
            B = mult(A,B)
        A = mult(A,A)
        m//=2
    return mult(A,B)
    
def calc_nth_term(init,linear_coeff,n):
    def mult(A,B):
        return polymod(polyprod(A,B),linear_coeff)
    
    ans = power([0,1],[1],n,mult)
    return sum(ans[i]*init[i] for i in range(len(ans)))


n,m = [int(x) for x in input().split()]

linear_rec = [0]*(m+1)
linear_rec[0] = -1
linear_rec[m-1] = -1
linear_rec[m] = 1

print(calc_nth_term([1]*m,linear_rec,n)%MOD)