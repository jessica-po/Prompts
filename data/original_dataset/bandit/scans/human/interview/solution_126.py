# A

input()
l = list(map(int, list(input())))

if (1 in l or 4 in l or 7 in l or 0 in l) and (1 in l or 2 in l or 3 in l) and (3 in l or 6 in l or 9 in l or 0 in l) and (7 in l or 0 in l or 9 in l):
    print("YES")
else:
    print("NO")