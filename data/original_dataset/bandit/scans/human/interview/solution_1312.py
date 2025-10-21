n,m = map(int,input().split())
a = n % m;
for i in range(m - a):
    print(n//m,end =' ')
for i in range(a):
    print(n//m+1,end = ' ')