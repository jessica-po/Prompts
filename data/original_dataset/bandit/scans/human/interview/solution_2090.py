import heapq

n,k=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(n)]

S.sort(key=lambda x:x[1],reverse=True)

ANS=0
LENGTH=0
H=[]

for x,y in S:
    heapq.heappush(H,x)
    LENGTH+=x
    if len(H)>k:
        z=heapq.heappop(H)
        LENGTH-=z
        
    if ANS<LENGTH*y:
        ANS=LENGTH*y

print(ANS)