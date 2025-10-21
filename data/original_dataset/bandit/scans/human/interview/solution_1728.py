n = int(input())

T = [int(x) for x in input().split()]

C = [int(x) for x in input().split()]

T_inv = [[] for _ in range(n)]

for i in range(n - 1):
    T_inv[T[i] - 1] += [i + 1]

result = 1

#for i in range(n):
#    print(T_inv[i])

for i in range(n):
    for child in T_inv[i]:
        if C[i] != C[child]:
            result += 1

print(result)