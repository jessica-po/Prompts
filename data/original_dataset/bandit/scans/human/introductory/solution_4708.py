N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if K < N:
    ans = K*X + (N-K)*Y
else:
    ans = N*X
print(ans)