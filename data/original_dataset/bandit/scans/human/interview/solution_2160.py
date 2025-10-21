nCells, nQueries = list(map(int, input().split()))
queries = list(map(int, input().split()))
seen = [False] * 100002
bad = set()
for q in queries:
    if not seen[q]:
        seen[q] = True
        bad.add((q, q))
    if seen[q - 1]:
        bad.add((q - 1, q))
    if seen[q + 1]:
        bad.add((q + 1, q))
print((nCells - 1) * 2 + nCells - len(bad))