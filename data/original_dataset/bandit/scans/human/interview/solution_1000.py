n,v = map(int,input().split())
req = n-1

if req<=v:
    print (req)
else:
    total = v
    remaining = req-v
    for x in range(remaining):
        total += 2+x
    print (total)