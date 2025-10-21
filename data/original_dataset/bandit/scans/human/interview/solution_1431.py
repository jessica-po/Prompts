N = int(input())
A = tuple(map(int, input().split(' ')))

bits = [0] * (N + 1)

i = N
while i > 0:
    j = i
    ones = 0
    while j <= N:
        ones += bits[j]
        j += i
    if ones % 2 != A[i - 1]:
        bits[i] = 1
    i -= 1

indexes = []
for i in range(1, N + 1):
    if bits[i] == 1:
        indexes.append(i)

print((len(indexes)))
if indexes:
    print((*indexes))