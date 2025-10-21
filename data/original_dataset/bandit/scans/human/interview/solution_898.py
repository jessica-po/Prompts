from bisect import bisect_left,bisect

# ===================================== 約数のリスト   
def enum_div(n):
    ir=int(n**(0.5))+1
    ret=[]
    for i in range(1,ir):
        if n%i == 0:
            ret.append(i)
            if (i!= 1) & (i*i != n):
                ret.append(n//i)
    return ret

n,m=list(map(int,input().split()))

div=enum_div(m)+[m]
div.sort(reverse=True)

rd=[0]*len(div)
for i in range(len(div)):
    rd[i]=m//div[i]

mm=bisect_left(rd,n)

print((div[mm]))