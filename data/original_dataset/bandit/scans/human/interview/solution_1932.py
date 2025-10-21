import sys

cnt = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20}

n = int(input())
c = 0

for _ in range(n):
    s = input()
    c += cnt[s]

print(c)