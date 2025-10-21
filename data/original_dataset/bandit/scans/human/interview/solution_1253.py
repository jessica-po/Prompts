rd = lambda: list(map(int, input().split()))
k = kk = rd()[1]
a = rd()
k -= sum(x<0 for x in a)
a[:kk] = list(map(abs, a[:kk]))
print(sum(a)-(2*min(a) if k>0 and k%2 else 0))