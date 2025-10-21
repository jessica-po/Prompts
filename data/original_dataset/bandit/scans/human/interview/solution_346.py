n, m =  list(map(int, input().split()))
prices =  list(map(int, input().split()))
auci = list(map(int, input().split()))

scores = 0

# m auc
# n - m default

for i in range(len(prices)):
    if (i+1) not in auci:
        scores += prices[i]
        prices[i] = 0

ra = []
for i in prices:
    if i != 0:
        ra.append(i)
ra.sort()
ra = ra[::-1]

for i in ra:
    if i > scores:
        scores += i
    else:
        scores *= 2

print(scores)
#print(ra)