rd = lambda: list(map(int, input().split()))

n, k = rd()
print(' '.join(map(str, list(range(n, n-k,-1))+list(range(1,n-k+1)))))