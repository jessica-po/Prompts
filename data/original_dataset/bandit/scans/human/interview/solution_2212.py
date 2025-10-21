n=int(input())
magic=int((n-1)/2)
x = []
for t in range(magic, -1, -1):
    x.append(t*'*'+'D'*(n-2*t)+t*'*')
for u in range(1, magic+1):
    x.append(u*'*'+'D'*(n-2*u)+u*'*')

no = 1
ne = 2
for i in range(n):
    for j in range(n):
        if (x[i][j] == 'D'):
            print(no, end = ' ')
            no += 2
        else:
            print(ne, end = ' ')
            ne += 2
    print()