j,s,m=map(int,input().split())
if ((m-j)//s)%2!=0:
    print('Unlucky Chef')
else:
    print('Lucky Chef')