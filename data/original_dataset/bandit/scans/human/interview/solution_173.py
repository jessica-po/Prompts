a, b = list(map(int, input().split(' ')))
hor = input()
ver = input()
if (hor[0], ver[0]) == ('>', 'v') or (hor[0], ver[-1]) == ('<', 'v'):
    print("NO")
elif (hor[-1], ver[0]) == ('>', '^') or (hor[-1], ver[-1]) == ('<', '^'):
    print("NO")
else:
    print("YES")