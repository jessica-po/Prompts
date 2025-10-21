n=int(input())

if(n<=2):
    print(-1)

else:
    for i in range(n,1,-1):
        print(i,end=" ")
    print(1)