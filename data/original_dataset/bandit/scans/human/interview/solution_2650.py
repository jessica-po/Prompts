from heapq import heappop, heappush
n , q = map(int,input().split())
enzi = [[0,0] for i in range(n)]
youti = [[] for i in range(2*10**5)]
saikyo = [0 for i in range(2*10**5)]
ans = []

for i in range(n):
    a , b = map(int,input().split())
    enzi[i] = [a,b-1]
    heappush(youti[b-1],(-a,i))

for i in range(2*10**5):
    if youti[i]:
        now = heappop(youti[i])
        saikyo[i] = -now[0]
        heappush(ans,(-now[0],i))
        heappush(youti[i],now)

for _ in range(q):
    c , d = map(lambda x:int(x)-1,input().split())
    heappush(youti[d],(-enzi[c][0],c))
    moto = enzi[c][1]
    enzi[c][1] = d
    
    while True:
        if youti[moto]:
            now = heappop(youti[moto])
            if enzi[now[1]][1] == moto:
                if saikyo[moto] != -now[0]:
                    saikyo[moto] = -now[0]
                    heappush(ans,(-now[0],moto))
                heappush(youti[moto],now)
                break
        else:
            saikyo[moto] = 0
            break
    while True:
        now = heappop(youti[d])
        if enzi[now[1]][1] == d:
            if saikyo[d] != -now[0]:
                saikyo[d] = -now[0]
                heappush(ans,(-now[0],d))
            heappush(youti[d],now)
            break
    
    while True:
        now = heappop(ans)
        if saikyo[now[1]] == now[0]:
            print(now[0])
            heappush(ans,now)
            break