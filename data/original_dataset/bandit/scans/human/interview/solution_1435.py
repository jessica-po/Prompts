s=input()
ans=0

i=1
past=int(s[0])
c=1
ans=1
while(i<len(s)):
    if(int(s[i])+past==9):
        c+=1
        past=int(s[i])
    else:
        if(c%2==1 and c!=1):
            ans*=(c//2+1)
        c=1
        past=int(s[i])
    i+=1
if(c!=1 and c%2==1):
    ans*=(c//2+1)

    
print(ans)