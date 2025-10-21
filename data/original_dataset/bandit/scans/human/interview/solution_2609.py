import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    intervals = [None]*n
    for i in range(n):
        intervals[i] = tuple([int(a) for a in sys.stdin.readline().split()])
    intervals = list(zip(intervals, list(range(n))))
    starts = sorted(intervals, key = lambda x: x[0][0])
    ends   = sorted(intervals, key = lambda x: x[0][1])

    connects = [0]*n
    gaps = 0
    covering = set()
    atS = 0
    atE = 0
    # print(starts)
    while atE<n:
        # print("%d, %d"%(atS, atE))
        # print(covering)
        # print(connects)
        if atS!=n and ends[atE][0][1]>=starts[atS][0][0]:
            if len(covering)==1:
               gap = list(covering)[0]
               connects[gap]+=0.5
            covering.add(starts[atS][1])
            atS += 1
            if len(covering)==1:
               gap = list(covering)[0]
               connects[gap]-=0.5

        else:
            if len(covering)==1:
               gap = list(covering)[0]
               connects[gap]-=0.5
            covering.remove(ends[atE][1])
            atE += 1
            if len(covering)==1:
               gap = list(covering)[0]
               connects[gap]+=0.5
            if len(covering)==0:
                gaps += 1
    connects = [int(a) for a in connects]
    print(max(connects)+gaps)