h,w=list(map(int,input().split()))
dx=[0,1,0,-1] ; dy=[1,0,-1,0]
A=[list(input()) for i in range(h)]

for i in range(h):
    for  j in range(w):
        if A[i][j]=="#":
            for q,e in zip(dx,dy):
                if 0<=i+q<h and 0<=j+e<w:
                    if A[i+q][e+j]=="#":break
            else:
                print("No");return
print("Yes")