l = 0
r = -1
segL, time = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
segSum = 0
segments = []

##while r < segL-1:	
##    r += 1
##    segSum += a[r]
##    if segSum == time:
##        segments.append(r+1-l)
##    elif segSum > time:
##        segments.append(r-l)
##        while segSum > time or l < r:
##            # Shifting l to the right
##            # until reaching next suitable segment sum
##            segSum -= a[l]
##            l += 1
##        #segments.append(r+1-l)
##
##[1,2,5,3,7,4,5]

while r < segL-1:
    r += 1
    segSum += a[r]
    if segSum == time:
        segments.append(r+1-l)
        segSum -= a[l]
        l += 1
    elif segSum > time:
        segments.append(r-l)
        while segSum >= time:
            segSum -= a[l]
            l += 1
else:
    segments.append(r+1-l)

print(max(segments))