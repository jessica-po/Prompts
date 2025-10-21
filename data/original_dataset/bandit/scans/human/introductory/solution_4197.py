N = int(input())
A = list(map(int, input().split()))
dct = dict(enumerate(A))
ad = sorted(dct.items(), key=lambda x:x[1])
ans = []
for i in ad:
    j = i[0] + 1
    ans.append(j)
a = map(str, ans)
b = ' '.join(a)
print(b)