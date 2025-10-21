import fractions

n = int(input())
A = [int(x) for x in input().split()]
B = []
for i in range(n-1):
    B.append(A[i])
    if fractions.gcd(A[i], A[i+1]) != 1:
        B.append(1)
B.append(A[-1])
print(len(B) - n)
print(' '.join(map(str, B)))