inpt=input().split(' ')
n=int(inpt[0])
k=int(inpt[1])
i_lst=[]
j_lst=[]
m=0
inpt=input().split(' ')
for i in range(len(inpt)):
    inpt[i]=int(inpt[i])
for i in range(k):
    mn=min(inpt)
    mx=max(inpt)
    if mn!=mx:
        i_mn=inpt.index(mn)
        i_mx=inpt.index(mx)
        inpt[i_mn]+=1
        inpt[i_mx]-=1
        i_lst.append(i_mx)
        j_lst.append(i_mn)
        m+=1
    else:
        break
#print(inpt)
instblity=max(inpt)-min(inpt)
print(str(instblity)+' '+str(m))
for i in range(len(i_lst)):
    print(str(i_lst[i]+1)+' '+str(j_lst[i]+1))