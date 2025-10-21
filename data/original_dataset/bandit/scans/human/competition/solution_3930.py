n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
cumsum = [0]

for a in A:
   cumsum.append(cumsum[-1] + a)
#print(cumsum)
pows = set([k**i for i in range(50)])
cum = dict({})
cum[0] = 1

res = 0

for x in cumsum[1:]:
    for pow in pows:
        if (x - pow) in cum:
            res += cum[x - pow]
    if x in cum:
        cum[x] += 1
    else:
        cum[x] = 1

print(res)