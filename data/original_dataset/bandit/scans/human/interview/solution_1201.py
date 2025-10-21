n = int(input())

items = []
max_time = 0

for i in range(1,n+1):
    t,d,p = list(map(int,input().split()))
    max_time = max(max_time, d)
    items.append((t,d,p,i))

items.sort(key=lambda x: x[1])

dp = [[(0,[]) for _ in range(n+1)] for _ in range(max_time+1)]

for time in range(1, max_time+1):
    for it in range(1, n+1):
        
        if time < items[it-1][0] or time >= items[it-1][1]:
            dp[time][it] = max(dp[time][it-1], dp[time-1][it])
        else:
            
            pick = dp[time-items[it-1][0]][it-1][0] + items[it-1][2]
            if dp[time][it-1][0] > pick : 
                dp[time][it] = max(dp[time][it-1], dp[time-1][it])
            else:
                
                dp[time][it] = (dp[time-items[it-1][0]][it-1][0] + items[it-1][2], list(dp[time-items[it-1][0]][it-1][1]))
                dp[time][it][1].append(items[it-1][3])

#print(dp)

res = max(dp[max_time])

print(res[0])
print(len(res[1]))
print(*res[1])