X,A,B=list(map(int,input().split()))
if A-B>=0:
    print("delicious")
elif -A+B<=X:
    print("safe")
else:
    print("dangerous")