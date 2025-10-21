def f(n):
    if n==1:return[1]
    if n==2:return[1,2]
    if n==3:return[1,1,3]
    if n>3:
        L=f(n//2)
        for i in range(len(L)):L[i]*=2
        return [1]*(n-n//2)+L
L=f(int(input()))
s=''
for i in L:s+=(str(i)+' ')
print(s)