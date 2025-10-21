n = int(input())
vs = [int(x) for x in input().split()]
ts = [int(x) for x in input().split()]

sumt = 0
for i, t in enumerate(ts):
    vs[i]+=sumt
    sumt+=t

vs.sort()

tl, tr = 0, 0
il, ir = 0, 0
for ind, t in enumerate(ts): #check
    tl = tr
    tr += t
    while ir < n and vs[ir] <= tr: ir += 1
    cur_sum = 0
    while il < ir:
        cur_sum += vs[il]-tl
        il+=1
##    print(ir, tl, tr,  cur_sum)
    cur_sum += t * ((n-ir) - (n-ind-1))
    print(cur_sum, end=" ")