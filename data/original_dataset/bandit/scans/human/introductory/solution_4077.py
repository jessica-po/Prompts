MAXN = 200001

def less_sum(s, m):
    n = len(s)
    a = 0
    b = 0
    res = 0
    last = 0

    count = [0 for i in range(-MAXN, MAXN+1)]

    count[0] = 1
    x = 0
    last = 1

    for i in range(n):
        if s[i] > m:
            b += 1
        else:
            a += 1
        x = a-b
        #print(x)
        #print(count[-2], count[-1], count[0], count[1], count[2])
        if s[i] > m:
            last -= count[x+1]
        else:
            last += count[x]
        #print(x, last)
        res += last
        count[x] += 1
        last += 1
    
    #print(res)

    return res

n, m = map(int, input().split(' '))
s = list(map(int, input().split(' ')))[0:n]

#print(m, s)

print(less_sum(s, m) - less_sum(s, m-1))