N,K=input().split()
N,K=int(N),int(K)

if(N%2==0):
    if(K<=N//2):
        print(2*K-1)
    else:
        K-=N//2
        print(2*K)

else:
    if(K<=N//2+1):
        print(2*K-1)
    else:
        K-=N//2+1
        print(2*K)