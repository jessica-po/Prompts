def solve(a):
    seen = set()
    for i in range(len(a)):
        c = 0
        for j in range(i+2,len(a)):
            c += a[j-1]
            if a[i]^a[j] == c:
                seen.add((i,j))
            if c >= 2*a[i]:
                break
    
    for i in range(len(a)-1,-1,-1):
        c = 0
        for j in range(i-2,-1,-1):
            c += a[j+1]
            if a[i]^a[j] == c:
                seen.add((j,i))
            if c >= 2 *a[i]:
                break
    print(len(seen))
            


n = int(input())
a = list(map(int,input().split()))
solve(a)