N, K = map(int, input().split())
S = input()
print("".join(c.lower() if i == K else c for i, c in enumerate(S, 1)))