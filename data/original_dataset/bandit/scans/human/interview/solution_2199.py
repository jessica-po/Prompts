q=int(input())
s=input().split()
a=[int(s[1])]
sum1=a[0]
pos=-1
mean=sum1
fin=''
for i in range(q-1):
    n=len(a)
    s=input().split()
    if(s[0]=='1'):
        a.append(int(s[1]))
        sum1+=(a[-1]-a[-2])
        mean=sum1/(pos+2)
        n=len(a)
    
        #print(sum1,pos,i+1)
        while(pos<n-2 and a[pos+1]<mean):
            pos+=1
            sum1+=a[pos]
            
            mean=sum1/(pos+2)
        #print(sum1,pos,i+1)
    else:
        #print(sum1,pos)
        fin+=str(a[-1]-mean) + '\n'
print(fin)