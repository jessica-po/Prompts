K = int(input())
print(("-1" if K & 1 else "".join(["wb\n"[2 if k == K else (min(j, k, K - 1 - j,
    K - 1 - k) ^ i) & 1] for i in range(2) for j in range(K) for k in range(K +
        1)]) * (K >> 1)))