#python33
def program():
    num=-1
    R=[]
    L=[]
    n=int (eval(input ()))
    for i in range(n):
        l,r=((list(map(int,input().split()))))  
        R.append(r)
        L.append(l)  
    MAXR=max(R)
    MINL=min(L)

    for i in range(n):
        if R[i] == MAXR and L[i] == MINL:
            print(i+1)
            return 

    print(num)    
program()