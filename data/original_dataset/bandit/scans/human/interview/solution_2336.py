n, k, q = list(map(int, input().split()))
recipe_in = []
for i in range(n):
    l, r = list(map(int, input().split()))
    recipe_in.append((l, r))

query_in = []
for i in range(q):
    l, r = list(map(int, input().split()))
    query_in.append((l, r))

MAX = 200000 + 10
recipes = [0 for i in range(MAX)]
for recipe in recipe_in:
    l, r = recipe
    recipes[l] += 1
    recipes[r + 1] -= 1
for i in range(1, MAX):
    recipes[i] += recipes[i - 1]

cnts = [0 for i in range(MAX)]
for i in range(MAX):
    if recipes[i] >= k:
        cnts[i] += 1
for i in range(1, MAX):
    cnts[i] += cnts[i - 1]

for query in query_in:
    l, r = query
    ans = cnts[r] - cnts[l - 1]
    print(ans)