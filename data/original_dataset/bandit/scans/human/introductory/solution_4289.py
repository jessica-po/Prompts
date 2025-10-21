N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

high = []
abso = []
for i in range(N):
    high.append(T - (H[i] * 0.006))

n = 0
while n <= N - 1:
    abso.append(abs(A - high[n]))
    n += 1

answer = abso.index(min(abso)) + 1
print(answer)