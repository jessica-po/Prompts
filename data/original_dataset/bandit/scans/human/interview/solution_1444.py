from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
a = sorted([(a[x],str(x+1)) for x in range(n)])
k = int(stdin.readline())

sums = [0]
for x in a:
    sums.append(sums[-1]+x[0])

total = 0
s = 0

for x in range(k):
    total += a[x][0]*x-s
    s += a[x][0]

low = total
lowInd = 0

#print(total)

for x in range(n-k):
    s -= a[x][0]
    total -= s-a[x][0]*(k-1)
    total += a[x+k][0]*(k-1)-s
    s += a[x+k][0]
    if total < low:
        low = total
        lowInd = x+1

out = []

for x in range(lowInd,lowInd+k):
    out.append(a[x][1])
print(' '.join(out))