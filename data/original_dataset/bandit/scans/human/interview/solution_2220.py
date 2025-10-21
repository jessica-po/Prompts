n,m,k = map(int,input().split())
a = list(map(int,input().split()))

a = sorted(a)
b1 = a[-1]
b2 = a[-2]

k+=1
total = m//k
score = 0
score += (m%k) * b1
score += b1 * (total*(k-1))
score += b2 * total
print (score)