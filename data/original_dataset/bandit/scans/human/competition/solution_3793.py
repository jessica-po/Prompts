import itertools
from itertools import permutations as perm

l = [[int(x) for x in input().split()] for i in range(8)]

def dist2(p0,p1):
    return sum([(p0[i]-p1[i])**2 for i in range(3)])

def check(c):
    dists = [[(c[i][0]-c[j][0])**2+(c[i][1]-c[j][1])**2+(c[i][2]-c[j][2])**2 for i in range(8)] for j in range(8)]
    s2 = min([min(l) for l in dists])
    return all([sorted(l) == [0,s2,s2,s2,2*s2,2*s2,2*s2,3*s2] for l in dists])

def sub(p0,p1):
    return [p0[i]-p1[i] for i in range(3)]

def add(p0,p1):
    return [p0[i]+p1[i] for i in range(3)]

def div(p0,x):
    return [p0[i]//x for i in range(3)]

def cross(p0,p1):
    return [p0[(i+1)%3]*p1[(i+2)%3]-p0[(i+2)%3]*p1[(i+1)%3] for i in range(3)]

def match(p0,p1):
    return sorted(p0) == sorted(p1)

def poss(i,prior,s):
    if i == len(l): return check(prior)
    for p in perm(l[i]):
        if i == 1: print(p)
        possible = True
        for p2 in prior:
            if dist2(p,p2) not in [s,2*s,3*s]:
                possible = False
                break
        if possible:
            if poss(i+1,prior+[p]): return True
    return False

solved = False
for l2 in perm(l,3):
    p0 = l2[0]
    for p1 in perm(l2[1]):
        s2 = dist2(p0,p1)
        if s2 == 0: continue
        s = round(s2**.5)
        if s**2 != s2: continue
        for p2 in perm(l2[2]):
            if dist2(p0,p2) != s2 or dist2(p1,p2) != 2*s2: continue
            p3 = sub(add(p1,p2),p0)
            x = div(cross(sub(p1,p0),sub(p2,p0)),s)
            p4,p5,p6,p7 = add(p0,x),add(p1,x),add(p2,x),add(p3,x)
            l3 = [p0,p1,p2,p3,p4,p5,p6,p7]
            if sorted([sorted(p) for p in l]) == sorted([sorted(p) for p in l3]):
                print("YES")
                used = [False for i in range(8)]
                for p in l:
                    for i in range(8):
                        if used[i]: continue
                        if match(p,l3[i]):
                            print(l3[i][0],l3[i][1],l3[i][2])
                            used[i] = True
                            break
                solved = True
                break
        if solved: break
    if solved: break

if not solved: print("NO")
#if not poss(1,[l[0]]): print("NO")