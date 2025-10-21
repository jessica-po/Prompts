n = int(input())

tab = [int(x) for x in input().split()]

if n < 2 or (n == 2 and tab[0] == tab[1]):
    print(-1)
else:
    print(1)
    print(tab.index(min(tab)) + 1)