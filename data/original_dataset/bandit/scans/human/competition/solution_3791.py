def main():
    n=int(input())
    A=list(map(int,input().strip().split(' ')))

    def brutal(A):
        n=len(A)
        for i in range(n):
            temp=0
            pos=0
            neg=0
            for j in range(n):
                temp+=abs(A[j]-(j+i)%n)
                if A[j]-(j+i)%n>0:
                    pos+=1
                else:
                    neg+=1

            print(temp,i,pos,neg,'ans,shift,+ve,-ve')    


    for i in range(len(A)):
        A[i]-=1

    ans=0
    pos=0
    neg=0
    change=[0 for i in range(len(A))]

    for i in range(len(A)):
        ans+=abs(A[i]-i)
        if A[i]-i>0:
            pos+=1
        else:
            neg+=1
        if A[i]-i>0:
            change[i]=A[i]-i
        elif A[i]==i:
            change[i]=0
        else:
            if A[i]!=0:
                change[i]=A[i]+n-i
            else:
                change[i]=0
    MIN=ans
    index=0
    #print(ans)
    collect=[[] for i in range(n)]
    for x in range(len(change)):
        collect[change[x]]+=[x]
    #print(collect)

    #print(ans,pos,neg)    
    for s in range(1,n):  
        ans-=abs(A[n-s]-n+1)
        ans+=abs(A[n-s]-0)
        neg-=1

        ans-=pos
        ans+=neg
        if A[n-s]>0:
            pos+=1
        else:
            neg+=1


        pos-=len(collect[s])
        neg+=len(collect[s])
        #print(ans,pos,neg)
        if ans<MIN:
            MIN=ans
            index=s
    print(MIN,index)        
    #brutal(A)        
main()