n = int(input())
a = []
for i in range(n):
    inp = input().split()
    a.append((int(inp[0]),int(inp[1])))
#End of Input Part

first = []
second = []
for i in range(n):
    first.append(a[i][0])
    second.append(a[i][1])

# Sort Them
first.sort(reverse = True)
second.sort()

bestAnswer = 0
for i in range(n):
    l = first[0]
    r = second[0]
    if(l==a[i][0]):
        l = first[1]
    if(r==a[i][1]):
        r = second[1]
    curLength = r-l
    bestAnswer = max(bestAnswer,curLength)

#Print Answer
print(bestAnswer)