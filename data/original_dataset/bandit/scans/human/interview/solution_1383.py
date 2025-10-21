n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [u % m for u in a]
b = [u % m for u in b]
a.sort()
b.sort()
possible = set(sorted([(b[0] - u + m) % m for u in a])) # At most 2000 elements
# O(n^2)
for x in possible:
    array = [(u + x) % m for u in a]
    if sorted(array) == b:
        print (x)
        break