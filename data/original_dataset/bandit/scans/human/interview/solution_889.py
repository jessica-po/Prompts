L=[]
for i in range(4):
    L.append(input())
ans="NO"
for i in range(3):
    for j in range(3):
        x=L[i][j]+L[i][j+1]+L[i+1][j]+L[i+1][j+1]
        if(x.count('#')==3 or x.count('.')==3 or x.count('#')==4 or x.count('.')==4):
            ans="YES"
print(ans)