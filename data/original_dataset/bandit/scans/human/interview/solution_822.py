n, m, z = list(map(int, input().split()))
print(sum(1 for t in range(1, z + 1) if t % n == 0 and t % m == 0))