n=int(input())
a=int(input())
b=int(input())
c=int(input())
r=n//a
if n > c:
    r=max(r,(r-b+c)//a+1,(n-c)//(b-c)+((n-c)%(b-c)+c)//a)
print(r)