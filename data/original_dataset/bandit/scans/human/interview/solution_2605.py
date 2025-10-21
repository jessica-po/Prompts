from sys import stdin


n, k = list(map(int, input().split()))
our = list(map(int, input().split()))
cap = set(map(int, input().split()))
res = 0
sum_b = sum(our)
for elem in cap:
    sum_b -= our[elem - 1]
    res += sum_b * our[elem - 1]
for i in range(len(our)):
    if (i + 1) not in cap and (i + 1) % n + 1 not in cap:
        res += our[i] * our[(i + 1) % n]
print(res)