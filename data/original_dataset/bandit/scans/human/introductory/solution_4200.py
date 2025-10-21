n, m = map(int, input().split())
a = list(map(int, input().split()))
get = 0
count = 0

for i in a:
    get += i

for i in a:
    if i*4*m >= get:
        count += 1

if count >= m:
    print("Yes")
else:
    print("No")