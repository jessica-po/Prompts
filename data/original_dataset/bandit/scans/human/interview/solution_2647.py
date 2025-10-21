import copy
h,w =list(map(int,input().split()))

s = [[]*w for _ in range(h)]
white =0
for i in range(h):
    t = input()
    for j in range(w):
        if t[j] == ".":
            white += 1
            s[i].append(10**5)
        elif t[j] == "#":
            s[i].append(t[j])
now = [0,0]
steps =[]
steps.append(now)
direction = []
s[0][0] =0
a = [2]
while len(steps) >0:
    now = copy.copy(steps[0])
    if s[now[0]][now[1]] =="#":
        continue
    for k in [[0,1],[1,0],[-1,0],[0,-1]]:
        now = copy.copy(steps[0])
        if now[0] + k[0] >=0 and now[0] + k[0] < h:
            now[0] += k[0]
            if now[1] + k[1] >=0 and now[1] + k[1] <w:
                now[1] += k[1]
                if s[now[0]][now[1]] == 10**5:
                    if not [now[0],now[1]] in steps:
                        steps.append([now[0],now[1]])
            else:
                continue
        else:
            continue
    # if s[steps[0][0]][steps[0][1]] ==0:
    #     steps.pop(0)
    #     continue
    if s[steps[0][0]][steps[0][1]] >10**4:
        direction =[]
        for l in [[0,1],[1,0],[-1,0],[0,-1]]:
            if steps[0][0]+l[0]>=0 and steps[0][0]+l[0]<h and steps[0][1]+l[1]< w and steps[0][1]+l[1] >=0 and s[steps[0][0]+l[0]][steps[0][1]+l[1]] != "#":
                s[steps[0][0]][steps[0][1]]=min(s[steps[0][0]+l[0]][steps[0][1]+l[1]]+1,s[steps[0][0]][steps[0][1]])
    steps.pop(0)
if s[h-1][w-1] == "#" or s[h-1][w-1] == 10**5:
    print((-1))
else:
    print((white-1 - s[h-1][w-1]))