a, b, n, x = list(map(int, input().split(' ')))
fir = pow(a, n, 10**9+7)*x%(10**9+7)
sec = b*(pow(a, n, 10**9+7)-1)*(pow(a-1, 10**9+5, 10**9+7))%(10**9+7)
if (a == 1):
    sec = n * b
print((fir+sec)%(10**9+7))