from array import array
inf = (1 << 30)

def main():
    (n,k) = [int(x) for x in input().split(' ')]
    Matrix = []
    for i in range(n):
        Matrix.append(array('b',[ord(x) for x in input()]))
    dp = [array('l', [inf for j in range(n)]) for i in range(n)]
    direct = [[ord('d') for j in range(n)] for i in range(n)]
    opt = ""
    for s in range (2 * n - 1):
        opchar = chr(ord('z') + 1)
        positions = []
        for i in range(0, s+1):
            j = s - i;
            if j < n and i < n:
                if(i > 0 and j > 0):
                    if(dp[i-1][j] < dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                        direct[i][j] = 'l'
                    else:
                       dp[i][j] = dp[i][j-1]
                       direct[i][j] = 'd'
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
                    direct[i][j] = 'l'
                elif j > 0:
                    dp[i][j] = dp[i][j-1]
                    direct[i][j] = 'd'
                else:
                    dp[i][j] = 0
                    direct[i][j] = 'e'
                if(dp[i][j] < k and Matrix[i][j] is not ord('a')):
                    dp[i][j]+=1
                    Matrix[i][j] = ord('a')
                if(Matrix[i][j] < ord(opchar) and dp[i][j] <= k):
                     opchar = chr(Matrix[i][j])
        for i in range(0, s+1):
            j = s - i;
            if j < n and i < n:
                if(Matrix[i][j] is not ord(opchar)):
                    dp[i][j] = inf
    ans = ""
    a,b = (n-1,n-1)
    while(direct[a][b] is not 'e'):
        ans += chr(Matrix[a][b])
        if(direct[a][b] is 'l'):
            a-=1
        else:
            b-=1
    ans += chr(Matrix[0][0])
    print(ans[::-1])

main()