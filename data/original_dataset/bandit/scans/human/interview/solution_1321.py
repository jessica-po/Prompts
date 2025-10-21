n = int(input())
wihi = [list(map(int,input().split())) for i in range(n)]
W = 0
H = 1
H1 = 1
num = 0
for i in wihi:
    W += i[0]
    H = max(H,i[1])
for i in range(n):
    if num == 0:
        if wihi[i][1] == H:
            num = 1
        else:
            H1 = max(H1,wihi[i][1])
    else:
        H1 = max(H1,wihi[i][1])
if H1 == H:
    for i in wihi:
        print((W - i[0]) * (H),end=" ")
else:
    for i in wihi:
        if i[1] == H:
            print((W - i[0]) * (H1),end=" ")
        else:
            print((W - i[0]) * (H),end=" ")