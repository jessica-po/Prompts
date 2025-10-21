X=[]
Y=[]
Points=[]
k=False
for i in range(8):
    x,y=list(map(int,input().split()))
    X.append(x)
    Y.append(y)
    if([x,y] in Points):
        k=True
    Points.append([x,y])
X.sort()
Y.sort()

if(len(set(X))!=3 or len(set(Y))!=3 or k):
    print("ugly")

elif(X.count(X[0])!=3 or X.count(X[3])!=2 or X.count(X[5])!=3):
    print("ugly")

elif(Y.count(Y[0])!=3 or Y.count(Y[3])!=2 or Y.count(Y[5])!=3):
    print("ugly")

elif([X[3],Y[3]] in Points):
    print("ugly")

else:
    print("respectable")