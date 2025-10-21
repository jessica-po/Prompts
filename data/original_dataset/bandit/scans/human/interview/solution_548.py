n = int(input())
a = list(map(int, input().split()))

nechet = 0

for el in a:
    if el % 2 == 1:
        nechet += 1

if nechet == 0:
    print('Second')
else:
    print('First')