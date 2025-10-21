f=lambda a:(a+1)%2

n=int(input())
a=list(map(int, bin(n)[2:].zfill(4)[::-1]))
a[3]=f(a[3])
if (a[3]): a[2]=f(a[2])
if a[3] and a[2]: a[1]=f(a[1])
if a[3] and a[2] and a[1]: a[0]=f(a[0])

print (int("".join(map(str, a))[::-1], 2))