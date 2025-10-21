n, B = list(map(int, input().split()))

A = [int(x) for x in input().split()]

odd, even = 0, 0

cuts = []

for i in range(n - 1):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    if odd == even:
        cuts += [(abs(A[i] - A[i + 1]), i)]

cuts.sort()

result = 0

for cost, _ in cuts:
    if cost <= B:
        B -= cost
        result += 1


print(result)