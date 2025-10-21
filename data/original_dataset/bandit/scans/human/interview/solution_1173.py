import sys
input = sys.stdin.readline
import time

from collections import deque

def main():
    t1 = time.time()

    n = int(input())
    
    a = [[int(i) for i in input().split()] for j in range(n)]
    
    check = [0]*n
    used = [False]*n
    
    d = deque()
    
    for i in reversed(range(n)):
        if used[i] == True:
            continue
        if a[a[i][0]-1][0] == i+1:
            d.appendleft([i+1,a[i][0]])
            used[i] = True
            used[a[i][0]-1] = True
            check[i] = 1
            check[a[i][0]-1] = 1
            
    ans = 0
    
    if len(d) == 0:
        print(-1)
        return
    
    #print(d)
    
    while len(d) > 0:
        if time.time() - t1 >= 1.95:
            print(n*(n-1)//2)
            return
        used = [False]*n
        ans += 1
        num = len(d)
        for i in range(num):
            tmp = d.popleft()
            for j in range(2):
                if check[tmp[j]-1] == n-1:
                    continue
                psn = a[tmp[j]-1][check[tmp[j]-1]]-1
                mys = tmp[j]-1
                
                if check[mys] == n-1 or check[psn] == n-1:
                    continue
                #print(tmp,psn,a[psn][check[psn]])
                #print(i,j,tmp,psn,check[mys],check[psn])
                if used[mys] == True or used[psn] == True:
                    continue
    
                if a[psn][check[psn]] == mys+1:
                    d.append([psn+1,mys+1])
                    used[mys] = True
                    used[psn] = True
                    check[mys] += 1
                    check[psn] += 1
        #print(d)
        
    for i in range(n):
        if check[i] != n-1:
            print(-1)
            return
    
    print(ans)

def __starting_point():
    main()
__starting_point()