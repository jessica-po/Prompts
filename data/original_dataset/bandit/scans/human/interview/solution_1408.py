3

n = int(input())
books = [[], []]
for _ in range(n):
    t, w = tuple(map(int, input().split()))
    books[t - 1].append(w)
for _ in range(2):
    books[_].sort()
#print(books)
ans = 10**9
for i in range(len(books[0]) + 1):
    for j in range(len(books[1]) + 1):
        hor = sum(books[0][:i]) + sum(books[1][:j])
        ver = len(books[0]) - i + 2 * (len(books[1]) - j)
        if hor <= ver and ver < ans:
            ans = ver
        #print(i, j, hor, ver, ans)
print(ans)