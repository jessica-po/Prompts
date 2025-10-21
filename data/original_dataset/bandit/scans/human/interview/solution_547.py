n, k = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(input())
s = input()
kmn = 1
kmx = 0
for i in range(n):
    if (len(a[i]) < len(s)):
        kmn += 1
        kmx += 1
    elif (len(a[i]) == len(s)):
        kmx += 1
print((kmn - 1) // k * 5 + kmn, (kmx - 1) // k * 5 + kmx)