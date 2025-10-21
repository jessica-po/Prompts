def f(n):
    a=0
    while(n>0):
        a+=n%10
        n//=10
    return a
n=int(input())
while f(n)%4!=0:
    n+=1
print(n)