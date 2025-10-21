# calculate convex of polygon v.
# v is list of complexes stand for points.
def convex(v, eps=1e-8):

    # fetch the seed point
    v.sort(key=lambda x:(x.real,x.imag))
    v = v[0:1] + sorted(v[1:], key=lambda x:(x-v[0]).imag/abs(x-v[0]))

    n = 1
    for i in range(2, len(v)):
        while n > 1 and ((v[n]-v[n-1])*(v[i]-v[n]).conjugate()).imag>-eps:
            n -= 1
        else:
            n += 1
            v[n] = v[i]

    v[n+1:] = []

    return v

# calculate the area of a polygon v, anti-clockwise.
# v is list of complexes stand for points.
def area(v):
    ans = 0
    for i in range(2, len(v)):
        ans += ((v[i]-v[i-1])*(v[i-1]-v[0]).conjugate()).imag
    return ans * 0.5

n = int(input())
v = [complex(*tuple(map(int, input().split()))) for i in range(0, n)]

w = convex(v)
n = len(w)

ans = 0

def tri(i, j, k): return abs(((w[i]-w[j])*(w[i]-w[k]).conjugate()).imag) * 0.5

for i in range(0, n):
    
    for j in range(i+2, n):

        if i == 0 and j == n-1: continue
        
        l = i + 1
        r = j
        while l < r-1:
            k = l+r>>1
            if tri(i, j, k) > tri(i, j, k-1):
                l = k
            else:
                r = k
                
        s1 = tri(i, j, l)

        l = j - n + 1
        r = i
        while l < r-1:
            k = l+r>>1
            if tri(i, j, k) > tri(i, j, k-1):
                l = k
            else:
                r = k
        
        s2 = tri(i, j, l)

        ans = max(ans, s1 + s2)

if n == 3:
    for p in v:
        if not p in w:
            w.append(p)
            ans = max(ans, area(w))
            w.pop()
        
print(ans)