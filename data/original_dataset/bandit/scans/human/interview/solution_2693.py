# cook your dish here
def findCombo(s,p,k):
    if k==1:
        if s==p:
            return [s]
        else:
            return []
    else:
        for i in range(1,s):
            if(p%i==0) and i<s:
                ans=findCombo(s-i,p//i,k-1)
                if len(ans)!=0:
                    ans.append(i)
                    return ans 
        return []
try:
    s,p,k = map(int,input().split())
    ans=findCombo(s,p,k)
    if len(ans)==0:
        print("NO")
    else:
        print(*ans)

except:
    pass