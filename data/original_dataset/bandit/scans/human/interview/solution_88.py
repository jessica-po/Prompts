def zero(strx):
    k = []
    str2 = list(strx)
    for i in range(1, len(str2)):
        str3 = str2[:]
        str3[i] = '0'
        k.append(''.join(str3))
    return k
a = []
for i in range(1, 64):
    a += zero('1'*i)

ct = 0
x, y = list(map(int, input().split(' ')))
for i in a:
    if x <= int(i, 2) <= y:
        ct+=1
print(ct)