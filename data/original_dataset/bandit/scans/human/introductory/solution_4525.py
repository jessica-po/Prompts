for _ in range(int(input())):
    n=int(input())
    if(n%4!=0):
        print('NO')
    elif(n%4==0):
        print('YES')
        a=[]
        for i in range(1,n//2+1):
            a.append(i*2)
        s=sum(a)
        s1=0
        for i in range(1,n//2):
            x=i*2-1
            a.append(x)
            s1+=x
        a.append(s-s1)
        print(*a)