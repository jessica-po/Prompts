L=[]
for i in range(5):
    s=input().split()
    L.append(list(s))

for i in range(5):
    for j in range(5):
        if(L[i][j]=="1"):
            row=i
            col=j

x=abs(row-2)+abs(col-2)
print(x)