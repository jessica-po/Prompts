###Prediction and Restriction
n,k=list(map(int,input().split()))
r,s,p=list(map(int,input().split()))
t=input()
win=[False]*n
def janken(char):
    if char=='r':
        return p
    elif char=='s':
        return r
    else:
        return s
cnt=0
for i in range(n):
    if i-k<0:
        point=janken(t[i])
        cnt+=point
        win[i]=True
    else:
        if t[i]!=t[i-k]:
            point=janken(t[i])
            cnt+=point
            win[i]=True
        else:
            if not win[i-k]:
                point=janken(t[i])
                cnt+=point
                win[i]=True

print(cnt)