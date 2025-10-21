a,b,c=list(map(int,input().split()))
k=int(input())

x=max(a,b,c)

print(((a+b+c)-x+x*(2**k)))