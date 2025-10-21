n,k=list(map(int,input().split()))
mod=998244353

NEXT={(0,1):2,(1,2):2}#ww or wh,point k,場合の数

for i in range(1,n):
    NOW=NEXT
    NEXT=dict()
    for key in NOW:
        
        

        if key[0]==0:
            if k-(n-i)*2<=key[1]<=k:
                NEXT[key]=NEXT.get(key,0)+NOW[key]
            if k-(n-i)*2<key[1]+1<=k:
                NEXT[(0,key[1]+1)]=NEXT.get((0,key[1]+1),0)+NOW[key]
                NEXT[(1,key[1]+1)]=NEXT.get((1,key[1]+1),0)+NOW[key]*2%mod


        else:
            if k-(n-i)*2<=key[1]<=k:
                NEXT[key]=NEXT.get(key,0)+NOW[key]
                NEXT[(0,key[1])]=NEXT.get((0,key[1]),0)+NOW[key]*2%mod

            if k-(n-i)*2<key[1]+2<=k:
                NEXT[(1,key[1]+2)]=NEXT.get((1,key[1]+2),0)+NOW[key]
        #print(NOW,NEXT)




ANS=0
for key in NEXT:
    if key[1]==k:
        ANS=(ANS+NEXT[key])%mod

print(ANS)