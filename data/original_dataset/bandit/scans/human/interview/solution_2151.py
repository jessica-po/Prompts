n=int(input())
for x in range(n):
    l=int(input())
    ar=input()
    a=int(ar[0])
    b=int(ar[1:])
    if(a<b):
        print("YES")
        print(2)
        print(a,b)
    else:
        print("NO")