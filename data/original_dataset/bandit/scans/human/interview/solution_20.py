s = input()
h = int(s[:2])
m = int(s[3:])

def ispalin(h, m):
    s = "%02d:%02d"%(h,m)
    return s == s[::-1]

for d in range(999999):
    if ispalin(h, m):
        print(d)
        break
    m+= 1
    if m == 60:
        h = (h+1)%24
        m = 0