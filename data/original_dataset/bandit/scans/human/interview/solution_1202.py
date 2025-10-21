n = int(input())
a = list(tuple(map(int,input().split())) for i in range(n))
#a.append(tuple(map(int,input().split())))
m = n // 2
c = list('1' for i in range(m))
d = list('1' for i in range(m))
#for i in range(n):print(a[i][0],a[i][1])
for i in range(m,n):
        if a[i][0] < a[n-i-1][1]:
            c.append('1')
        else:
            c.append('0')
        if a[n-i-1][0] > a[i][1]:
            d.append('1')
        else:
            d.append('0')
print(''.join(c))
print(''.join(d))