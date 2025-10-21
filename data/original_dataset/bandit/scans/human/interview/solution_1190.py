w1, h1, w2, h2 = list(map(int, input().split()))
print(2 * (h1 + h2) + w1 + w2 + abs(w1 - w2) + 4)