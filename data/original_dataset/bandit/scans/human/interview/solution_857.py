input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for x in a:
    if x in b:
        print(x, end=' ')
print()