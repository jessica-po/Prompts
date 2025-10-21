n = int(input())
a = list(map(int, input().split()))
a.sort()

inc = list()
dec = list()
for x in a:
    if inc and inc[-1] == x:
        if dec and dec[-1] == x:
            print('NO')
            return
        dec.append(x)
    else:
        inc.append(x)

print('YES')
print(len(inc))
for x in inc:
    print(x, end=' ')
print()
print(len(dec))
for x in reversed(dec):
    print(x, end=' ')
print()