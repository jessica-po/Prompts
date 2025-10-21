n,m,k = [int(x) for x in input().split()]

if k+2>n+m:
    print(-1)
else:
    if k >= n:
        alpha = m // (k-n+2)
    else:
        alpha = m * (n // (k+1))
    if k >= m:
        beta = n // (k-m+2)
    else:
        beta = n * (m // (k + 1))
    print(max(alpha, beta))