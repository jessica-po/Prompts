from sys import stdin, stdout

k = int(stdin.readline())
n, m = map(int, stdin.readline().split())
left, right, down, up = [], [], [], []
coordinates = []

for i in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    
    if x1 == x2:
        if y1 < y2:
            coordinates.append((x1, y1, x2, y2, i))
        else:
            coordinates.append((x2, y2, x1, y1, i))
    else:
        if x1 < x2:
            coordinates.append((x1, y1, x2, y2, i))
        else:
            coordinates.append((x2, y2, x1, y1, i))
    
    left.append(coordinates[-1])
    right.append(coordinates[-1])
    up.append(coordinates[-1])
    down.append(coordinates[-1])

left.sort(key = lambda x: (x[0], x[2]))
down.sort(key = lambda x: (x[1], x[3]))

challengers = [[], [], [], []]
cntl, cntr, cntd, cntu = map(int, stdin.readline().split())
label = 1

if cntl or not cntl:
    for i in range(cntl, -1, -1):
        if (left[i][0], left[i][2]) == (left[cntl][0], left[cntl][2]):
            challengers[0].append(left[i][-1])  
        else:
            break
        
    for i in range(cntl + 1, k):
        if (left[i][0], left[i][2]) == (left[cntl][0], left[cntl][2]) and left[i][2] > left[i][0]:
            label = 0
        
        if (left[i][0], left[i][2]) == (left[cntl][0], left[cntl][2]):
            challengers[0].append(left[i][-1])  
        else:
            break

if cntr or not cntr:
    for i in range(k - 1 - cntr, k):
        if (left[i][0], left[i][2]) == (left[k - 1 - cntr][0], left[k - 1 - cntr][2]):
            challengers[1].append(left[i][-1])
        else:
            break
    
    for i in range(k - 2 - cntr, -1, -1):
        if (left[i][0], left[i][2]) == (left[k - 1 - cntr][0], left[k - 1 - cntr][2]) and left[i][2] > left[i][0]:
            label = 0
        
        if (left[i][0], left[i][2]) == (left[k - 1 - cntr][0], left[k - 1 - cntr][2]):
            challengers[1].append(left[i][-1])
        else:
            break

#!!!!!!!!!!!

if cntd or not cntd:
    for i in range(cntd, -1, -1):
        if (down[i][1], down[i][3]) == (down[cntd][1], down[cntd][3]):
            challengers[2].append(down[i][-1])
        else:
            break
        
    for i in range(cntd + 1, k):
        if (down[i][1], down[i][3]) == (down[cntd][1], down[cntd][3]) and down[i][3] > down[i][1]:
            label = 0
            
        if (down[i][1], down[i][3]) == (down[cntd][1], down[cntd][3]):
            challengers[2].append(down[i][-1])  
        else:
            break
        
if cntu or not cntu:
    for i in range(k - 1 - cntu, k):
        if (down[i][1], down[i][3]) == (down[k - 1 - cntu][1], down[k - 1 - cntu][3]):
            challengers[3].append(down[i][-1])
        else:
            break
    
    for i in range(k - 2 - cntu, -1, -1):
        if (down[i][1], down[i][3]) == (down[k - 1 - cntu][1], down[k - 1 - cntu][3]) and down[i][3] > down[i][1]:
            label = 0
        
        if (down[i][1], down[i][3]) == (down[k - 1 - cntu][1], down[k - 1 - cntu][3]):
            challengers[3].append(down[i][-1])
        else:
            break

ans = set(challengers[0]) & set(challengers[1]) & set(challengers[2]) & set(challengers[3])

if not len(ans) or not label:
    stdout.write('-1')
else:
    stdout.write(str(list(ans)[0] + 1))