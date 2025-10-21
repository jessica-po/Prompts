A,B,K = map(int,input().split())
if A >= K:
    print(A-K,B)
elif K-A<B:
    print(0,B-(K-A))
else:
    print(0,0)