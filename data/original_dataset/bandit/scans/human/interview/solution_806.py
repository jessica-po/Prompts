MOD = 10**9 + 7

n, l, r = list(map(int, input().split()))

lr_counts = [(r-l+1)//3]*3
for i in range(l + sum(lr_counts), r + 1):
    lr_counts[i % 3] += 1

cur_counts = [1, 0, 0]
for _ in range(n):
    new_counts = [0, 0, 0]
    for j in range(3):
        for k in range(3):
            new_counts[(j + k) % 3] += cur_counts[j] * lr_counts[k]

    for j in range(3):
        cur_counts[j] = new_counts[j] % MOD


print(cur_counts[0])