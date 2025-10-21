n = int(input())
d = 367
F = [0 for i in range(d)]
M = [0 for i in range(d)]
for i in range(n):
    sex, l, r = input().split()
    l, r = int(l), int(r)
    if sex == 'F':
        for j in range(l, r+1): F[j] += 1
    else:
        for j in range(l, r+1): M[j] += 1
print(2*max(min(F[i], M[i]) for i in range(d)))