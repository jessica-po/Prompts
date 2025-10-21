stops, cap = map(int,input().split())

a = list(map(int,input().split()))

start_max = cap
start_min = 0

current = 0
for x in a:
    current += x
    start_max = min(cap-current, start_max)
    start_min = max(start_min,-current)
    if abs(current) > cap:
        print (0)
        break
else:
    if start_max<start_min:
        print (0)
    else:
        print (start_max-start_min + 1)