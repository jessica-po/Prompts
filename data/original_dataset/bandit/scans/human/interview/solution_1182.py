dhuang=0
a,b,c,d=list(map(int,input().split(' ')))
huang = [['*']*b for _ in range(a)]
for i in range(c):
    x,y=list(map(int,input().split(' ')))
    huang[x-1][y-1] = '#'
for i in range(a):
    for j in range(b):
        for k in range(i, a):
            for l in range(j, b):
                ct=0
                for m in range(i, k+1):
                    for n in range(j, l+1):
                        if huang[m][n]=='#':
                            ct+=1
                if ct>=d:
                    dhuang+=1
print(dhuang)