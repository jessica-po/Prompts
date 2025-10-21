3

szs = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
d = {'S':0, 'M':1, 'L':2, 'XL':3, 'XXL':4, 'XXXL':5}
neigh = [[] for i in range(5)]

of = list(map(int, input().split()))
n = int(input())
ans = ['' for i in range(n)]
for i in range(n):
    t = input()
    if ',' in t:
        neigh[d[t.split(',')[0]]].append(i)
    else:
        of[d[t]] -= 1
        ans[i] = t

for i in range(6):
    if of[i] < 0:
        print("NO")
        return
    if i > 0:
        while len(neigh[i - 1]) and of[i] > 0:
            ans[neigh[i - 1][-1]] = szs[i]
            neigh[i - 1].pop()
            of[i] -= 1
    if i < 5:
        while len(neigh[i]) and of[i] > 0:
            ans[neigh[i][-1]] = szs[i]
            neigh[i].pop()
            of[i] -= 1


if sum([len(neigh[i]) for i in range(5)]) != 0:
    print("NO")
else:
    print("YES")
    print("\n".join(ans))