aa=0
a, b, c, d = (list(map(int, input().split(' '))))

l = list(map(int, input().split(' ')))

for i in range(2**a):
    k = bin(i)[2:]
    t = 0
    k = '0' * (a-len(k)) + k
    x = []
    for j in range(a):
        if k[j] == '1':
            x.append(l[j])
            t += 1
            
    if t >= 2:
        if b <= sum(x) <= c and max(x) - min(x) >= d:
            aa+=1
print(aa)