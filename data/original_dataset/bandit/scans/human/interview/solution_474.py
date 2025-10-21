n = int(input())
a = list(map(int,input().split()))
m = max(a)

current = 0
longest = 0
for x in a:
    if x == m:
        current +=1
    else:
        longest = max(current,longest)
        current = 0
longest = max(current,longest)
print (longest)