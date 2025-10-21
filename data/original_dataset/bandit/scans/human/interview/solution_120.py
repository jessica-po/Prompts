import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())
if n%4: print("===")
else:
    t=input().strip()
    a=[n//4]*4
    for i in t:
        if i=='A': a[0]-=1
        elif i=='C': a[1]-=1
        elif i=='G': a[2]-=1
        elif i=='T': a[3]-=1
    if min(a)<0: print("===")
    else:
        out=[]
        for i in t:
            if i=='?':
                if a[0]:
                    out.append('A')
                    a[0]-=1
                elif a[1]:
                    out.append('C')
                    a[1]-=1
                elif a[2]:
                    out.append('G')
                    a[2]-=1
                elif a[3]:
                    out.append('T')
                    a[3]-=1
            else: out.append(i)
        print("".join(out))