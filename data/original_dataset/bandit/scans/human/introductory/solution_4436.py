#-------------Program--------------
#----Kuzlyaev-Nikita-Codeforces----
#-------------Round615-------------
#----------------------------------

t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for i in range(2,int(n**0.5)+2):
        if len(a)==2:
            a.append(n)
            break        
        if n%i==0:
            a.append(i)
            n//=i
    a=list(set(a))
    if len(a)==3 and a.count(1)==0:
        print('YES')
        a.sort()
        print(a[0],a[1],a[2])
    else:
        print('NO')