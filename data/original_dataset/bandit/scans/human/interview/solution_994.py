3

import sys

(n, m) = list(map(int, input().split()))

firstData = None 

maxHeight = -1

for i in range(m):
    (d, h) = list(map(int, input().split()))

    if firstData is None:
        firstData = (d, h)
    else:
        if (d - prevD) < abs(h - prevH):
            print ("IMPOSSIBLE")
            return
        maxH = max(h, prevH)
        minH = min(h, prevH)
        resource = d - prevD - (maxH - minH) # "free" days for going up-down
        possibleH = maxH + resource // 2
        maxHeight = max(maxHeight, possibleH)

    (prevD, prevH) = (d, h)
    lastData = (d, h)

maxHeight = max(maxHeight, firstData[1] + firstData[0] - 1)
maxHeight = max(maxHeight, lastData[1] + (n - lastData[0]))

print (maxHeight)