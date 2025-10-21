read = lambda: list(map(int, input().split()))
n = int(input())
a = list(read())
s = set()
for i in a:
    s.add(i)
f1 = len(s) < 3
f2 = len(s) == 3 and max(s) + min(s) == 2 * sorted(s)[1]
print('YES' if f1 or f2 else 'NO')