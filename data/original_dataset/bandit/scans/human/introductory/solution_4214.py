import itertools
n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

def factorization(n):
    if n == 1:
        return 1
    return n * factorization(n-1)

size = factorization(n)
a = list(itertools.permutations(l,n))
total = 0
for i in range(size):
    for j in range(n-1):
        x1 = a[i][j][0]
        x2 = a[i][j+1][0]
        y1 = a[i][j][1]
        y2 = a[i][j+1][1]
        x_total = (x1-x2)**2
        y_total = (y1-y2)**2
        total += (x_total + y_total)**.5
print(total/size)