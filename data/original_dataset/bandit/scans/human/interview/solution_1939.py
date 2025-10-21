N,k=map(int,input().split())

ind=0
for i in range(N):
    for j in range(N):
        if(j!=N-1):
            if(j==i):
                print(k,end=" ")
            else:
                print(0,end=" ")
        else:
            if(j==i):
                print(k)
            else:
                print(0)