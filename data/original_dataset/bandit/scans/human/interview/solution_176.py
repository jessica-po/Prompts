s=input()
ast=[int(i) for i in s.split(' ')]
k,a,b=ast[0],ast[1],ast[2]
s1=(a-1)//k
s2=b//k
print(s2-s1)