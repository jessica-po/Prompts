def lis(a):
    b = []
    for c in a:
        # if len(b) == 0 or c > b[-1]
        if len(b) == 0 or c > b[-1]:
            b.append(c)
        else:
            l = 0
            r = len(b)
            while l < r-1:
                m = l+r>>1
                # if b[m] <= c: l = m
                if b[m] < c: l = m
                else: r = m
            # if b[l] <= c: l += 1
            if b[l] < c: l += 1
            b[l] = c
        
    return len(b)
                    

n = int(input())

a = list(map(int, input().split()))

print(lis(a))