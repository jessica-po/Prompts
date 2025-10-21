import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,x=map(int,input().split())

def mult(a,b):
    # compute a*b
    c=[0]*128
    for i in range(128):
        for j in range(128):
            c[i^j]+=a[i]*b[j]
    return c

def quickpow(a,b):
    # compute a**b
    if b==1:
        return a
    if b&1:
        return mult(quickpow(mult(a,a),b//2),a)
    return quickpow(mult(a,a),b//2)

prob=list(map(float,input().split()))
prob+=[0.0]*(128-len(prob))

print("%.9f"%(1-quickpow(prob,n)[0]))