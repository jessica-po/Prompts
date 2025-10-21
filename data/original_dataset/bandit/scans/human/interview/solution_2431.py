import sys
input = sys.stdin.readline


G0=[[[[0]*5500 for i in range(6)] for j in range(6)] for k in range(6)]
G1=[[[[0]*5500 for i in range(6)] for j in range(6)] for k in range(6)]
G2=[[[[0]*5500 for i in range(6)] for j in range(6)] for k in range(6)]


for x in range(1,6):
    for y in range(1,6):
        for z in range(1,6):
            
            for i in range(1,5500):
                s=G0[x][y][z][max(0,i-x)]
                t=G1[x][y][z][max(0,i-y)]
                u=G2[x][y][z][max(0,i-z)]

                for j in range(5):
                    if j==s or j==t or j==u:
                        continue
                    else:
                        G0[x][y][z][i]=j
                        break

                for j in range(5):
                    if j==s or j==u:
                        continue
                    else:
                        G1[x][y][z][i]=j
                        break

                for j in range(5):
                    if j==s or j==t:
                        continue
                    else:
                        G2[x][y][z][i]=j
                        break

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

t=int(input())
for tests in range(t):
    n,x,y,z=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A=[]
    for a in B:
        if a<=5400:
            A.append(a)
        else:
            A.append(a%2520+2520)

    XOR=0

    for a in A:
        XOR^=G0[x][y][z][a]

    ANS=0
    for a in A:
        k=XOR^G0[x][y][z][a]

        if G0[x][y][z][max(0,a-x)]==k:
            ANS+=1

        if G1[x][y][z][max(0,a-y)]==k:
            ANS+=1

        if G2[x][y][z][max(0,a-z)]==k:
            ANS+=1

    print(ANS)