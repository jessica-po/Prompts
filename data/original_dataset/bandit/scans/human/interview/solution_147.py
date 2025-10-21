import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,a,b=map(int,input().split())

if a<b: a,b=b,a

if b==0:
    # 1 01 001 0001 ... is optimal, plus a long series of 0's
    print((n-1)*a)
else:
    # pascal's triangle thing
    pascal=[[1]*20005]
    for i in range(20004):
        newrow=[1]
        for j in range(1,20005):
            newrow.append(newrow[-1]+pascal[-1][j])
            if newrow[-1]>n: break
        pascal.append(newrow)
    def getcom(a,b):
        # return a+b choose b
        # if larger than n, return infinite
        if len(pascal[a])>b: return pascal[a][b]
        if b==0: return 1
        if b==1: return a
        return 100000005

    # start with the null node (prefix cost 0)
    # can split a node into two other nodes with added cost c+a+b
    # new nodes have prefix costs c+a, c+b
    # want n-1 splits in total
    n-=1    # now represents number of splits needed

    # binary search the last cost added
    lo=0
    hi=a*int((n**0.5)*2+5)

    while 1:
        mid=(lo+hi)//2
        # count stuff
        c0=0    # < mid
        c1=0    # = mid
        for i in range(mid//a+1):
            j=(mid-i*a)//b
            if (mid-i*a)%b!=0:
                # c0 += iC0 + (i+1)C1 + (i+2)C2 + ... + (i+j)Cj
                for k in range(j+1):
                    #print(mid,i,k)
                    c0+=getcom(i,k)
                    if c0>n: break
            else:
                for k in range(j):
                    #print(mid,i,k)
                    c0+=getcom(i,k)
                    if c0>n: break
                #print(mid,i,j,"c1")
                c1+=getcom(i,j)
        #print(mid,"is",c0,c1)
        if n<c0:
            hi=mid-1
        elif c0+c1<n:
            lo=mid+1
        else:
            # mid is correct cutoff
            lowcost=0   # sum of all cost, where cost < mid
            for i in range(mid//a+1):
                j=(mid-i*a)//b
                if (mid-i*a)%b!=0:
                    for k in range(j+1):
                        lowcost+=getcom(i,k)*(i*a+k*b)
                else:
                    for k in range(j):
                        lowcost+=getcom(i,k)*(i*a+k*b)
            temp=lowcost+(n-c0)*mid
            print(temp+n*(a+b))
            break