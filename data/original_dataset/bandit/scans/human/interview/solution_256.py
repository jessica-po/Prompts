a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))


x,y=list(map(int,input().split()))
z,w=list(map(int,input().split()))


Team1=False
Team2=False
if(a>w and a>y and d>x and d>z):
    Team1=True

if(c>w and c>y and b>x and b>z):
    Team1=True

if(((x>b and w>c) or (z>b and y>c)) and ((x>d and w>a) or (z>d and y>a))):
    Team2=True


if(Team1):
    print("Team 1")
elif(Team2):
    print("Team 2")
else:
    print("Draw")