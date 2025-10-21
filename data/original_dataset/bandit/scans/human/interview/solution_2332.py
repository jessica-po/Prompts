n, k, m = list(map(int, input().split()))
w = list(input().split())

lk = {}
for i in range(n):
    lk[w[i]] = i

c = list(map(int, input().split()))

m = [10**19] * k
gr = [0] * n

for i in range(k):
    g = list(map(int, input().split()))
    for j in g[1:]:
        m[i] = min(m[i], c[j - 1])
        gr[j - 1] = i

let = input().split()
res = 0
for word in let:
    res += m[gr[lk[word]]]

print(res)