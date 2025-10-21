from heapq import *
n=int(input())
q,ans,k=[],[],0
for i in range(n):
    ss=input()
    if ss!="removeMin": 
        s,mm=ss.split(); m=int(mm)
        if s=='insert':
            k+=1
            heappush(q,m)
        else:
            while k==0 or q[0]!=m:
                if k==0:
                    heappush(q,m)
                    ans+=['insert '+mm]
                    k+=1
                elif q[0]<m: 
                    k-=1
                    t=heappop(q)
                    ans+=['removeMin']
                else: 
                    k+=1
                    heappush(q,m)
                    ans+=['insert '+mm]
    else: 
        if k==0:
            ans+=['insert 1']
        else: 
            heappop(q)
            k-=1
    ans+=[ss]
print(len(ans))
print('\n'.join(ans))