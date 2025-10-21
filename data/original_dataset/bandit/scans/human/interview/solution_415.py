def prog():
    n = int(input())
    inp = list(map(int,input().split()))
    ans = 0
    for i in range(len(inp)):
        x,y = 0 ,0
        for j in range(i,len(inp)):
            x+=inp[j]
            y+=100
            if(x>y):
                ans = max(ans,(j-i)+1)
    print(ans)
prog()