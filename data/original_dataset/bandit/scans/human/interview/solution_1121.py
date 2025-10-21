import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))

ANS=[[-1]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if ANS[i][j]==-1:
            for koma in ["A","B","C","D","E","F"]:
                for k,l in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                    if 0<=k<n and 0<=l<m and ANS[k][l]==koma:
                        break
                else:
                    nkoma=koma
                    break

            MAXlength=1
            if nkoma=="A":                
                for length in range(1,101):
                    if i+length>=n or j+length>=m:
                        break
                    
                    for k,l in [(i-1,j+length),(i+length,j-1)]:
                        if 0<=k<n and 0<=l<m and ANS[k][l]==nkoma:
                            break
                        if 0<=i<n and ANS[i][j+length]!=-1:
                            break
                    else:
                        MAXlength=length+1

            elif nkoma=="B":
                for length in range(1,101):
                    if i+length>=n or j+length>=m:
                        break

                    flag=0
                    if 0<=i-1<n and ANS[i-1][j+length]=="A":
                        flag=1
                    if 0<=j-1<m and ANS[i+length][j-1]==nkoma:
                        break
                    if 0<=i<n and ANS[i][j+length]!=-1:
                        break

                    if flag==1:
                        MAXlength=length+1
                    else:
                        break
                

            for k in range(i,i+MAXlength):
                for l in range(j,j+MAXlength):
                    ANS[k][l]=nkoma

for a in ANS:
    print("".join(a))