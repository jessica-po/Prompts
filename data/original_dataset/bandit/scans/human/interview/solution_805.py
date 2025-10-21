N = int(input())
sush = [0] * 101
for i in range(1, N + 1) :
    l, r = [int(s) for s in input().split()]
    for j in range(l, r) :
        sush[j] = (1 if i == 1 else 0)
print(str(sum(sush)))