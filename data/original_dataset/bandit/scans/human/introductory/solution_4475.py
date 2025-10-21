t = int(input())
# a = list(map(int, input().split()))
for _ in range(t):
    a,b,x,y,n = map(int,input().split())
    
    options = []
    a2 = max(a-n,x)
    b2 = max(b-(n-(a-a2)),y)
    options.append(a2*b2)
    
    b2 = max(b-n,y)
    a2 = max(a-(n-(b-b2)),x)
    options.append(a2*b2)
    
    print(min(options))