import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,k = list(map(int, input().split()))
a = list(map(int, input()))
b = a[:k]
c = [b[i%k] for i in range(n)]
if tuple(a)>tuple(c):
    d = int("".join(map(str, b)))
    d += 1
    b = list(map(int, str(d)))
    c = [b[i%k] for i in range(n)]
print(len(c))
print("".join(map(str, c)))