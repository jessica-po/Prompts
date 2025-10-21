import sys

H, W = list(map(int, input().split()))
L = set()
for y in range(H):
    row = input().strip()
    i_sweet = row.find('S')
    i_gnome = row.find('G')
    if i_sweet == -1 or i_gnome > i_sweet:
        print(-1)
        return
    L.add(i_sweet - i_gnome)
print(len(L))