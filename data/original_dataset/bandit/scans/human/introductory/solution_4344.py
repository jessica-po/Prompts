n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
uniq = []
seen = set()
for i, x in enumerate(a):
    if x not in seen:
        seen.add(x)
        uniq.append((i + 1, x))

if len(uniq) < k:
    print('NO')
else:
    print('YES')
    b = [str(i) for i, _ in uniq[:k]]
    print(' '.join(b))