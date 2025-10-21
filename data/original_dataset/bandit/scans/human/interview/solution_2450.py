inp=lambda :map(int,input().split())
def sol():
    x,y,on,tw=inp()
    res=0
    for n in range(x):
        s=input()
        sm=0
        for n in s:
            if n=='.':
                sm+=1
            else:
                a=sm*on
                b=(sm//2)*tw+(sm%2)*on
                res+=min(a,b)
                sm=0
        a=sm*on
        b=(sm//2)*tw+(sm%2)*on
        res+=min(a,b)
    print(res)

for n in range(int(input())):
    sol()