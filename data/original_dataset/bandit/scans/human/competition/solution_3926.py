def main():
    n,m = list(map(int, input().split()))
    r,c = list(map(int, input().split()))
    L,R = list(map(int, input().split()))
    lab = [input() for _ in range(n)]
    
    r -= 1
    c -= 1
 
    inf = n*m+1
    dist = [[inf] * m for _ in range(n)]
    dist[r][c] = 0
    
    Q = [(r,c)]
    for x,y in Q:
        d = dist[x][y]
        if x < n - 1 and dist[x + 1][y] > d and lab[x + 1][y] == '.':
            dist[x + 1][y] = d
            Q.append((x + 1, y))
 
        if 0 < x and dist[x - 1][y] > d and lab[x - 1][y] == '.':
            dist[x - 1][y] = d
            Q.append((x - 1, y))
        
        if 0 < y and dist[x][y - 1] > d and lab[x][y - 1] == '.':
            dist[x][y - 1] = d + 1
            Q.append((x, y - 1))
        
        if y < m - 1 and dist[x][y + 1] > d and lab[x][y + 1] == '.':
            dist[x][y + 1] = d + 1
            Q.append((x, y + 1))
    ans=0
    for i in range(n):
        for j in range(m):
            d = dist[i][j]
            if d < inf:
                right = (d + (j - c))//2
                left =  (d - (j - c))//2
                if right <= R and left <= L:
                    ans+=1
    print(ans)
main()
#Code By:pajenegod