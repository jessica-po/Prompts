n=int(input())

L=list(map(int,input().split()))

ind=L.index(max(L))

L.remove(max(L))

x=max(L)

print(ind+1,x)