n,k = list(map(int, input().split()))
L = list(map(int, input().split()))
i = 1
while k > 0:
    k = k - i
    i += 1
k = k + i - 1
print(L[k-1])