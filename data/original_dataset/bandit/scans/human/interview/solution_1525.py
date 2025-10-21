def check(amidakuji,w):
    before=0
    flag=True
    for _ in range(w-1):
        if amidakuji&1==1 and before==1:
            flag=False
            break
        elif amidakuji&1==1:
            before=1
            amidakuji>>=1
        else:
            before=0
            amidakuji>>=1
    return flag

from sys import stdin
def main():
    #入力
    readline=stdin.readline
    mod=10**9+7
    h,w,k=map(int,readline().split())

    dp=[[0]*w for _ in range(h+1)]
    dp[0][0]=1
    for i in range(1,h+1):
        for bit in range(1<<(w-1)):
            if check(bit,w)==False:
                continue
            else:
                for j in range(w):
                    if j==0:
                        if bit&1==1:
                            dp[i][j+1]+=dp[i-1][j]
                        else:
                            dp[i][j]+=dp[i-1][j]
                    elif j==w-1:
                        if bit&1==1:
                            dp[i][j-1]+=dp[i-1][j]
                        else:
                            dp[i][j]+=dp[i-1][j]
                    else:
                        if bit&1==1:
                            dp[i][j-1]+=dp[i-1][j]
                            bit>>=1
                        else:
                            bit>>=1
                            if bit&1==1:
                                dp[i][j+1]+=dp[i-1][j]
                            else:
                                dp[i][j]+=dp[i-1][j]

                for j in range(w):
                    dp[i][j]%=mod

    print(dp[h][k-1])

def __starting_point():
    main()
__starting_point()