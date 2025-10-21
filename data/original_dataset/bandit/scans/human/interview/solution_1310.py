n = int(input()) + 1
t = [0] + list(map(int, input().split()))
for i in range(1, n):
    t[i] = t[i] ^ t[i - 1]
print(max(t[j] ^ t[i] for i in range(0, n) for j in range(i + 1, n)))