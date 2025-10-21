t = int(input())

for _ in range(t):
    s = [int(i) for i in input()]
    ct0 = 0
    ct1 = 0
    
    for i in s:
        if i == 1:
            ct1 += 1
        else:
            ct0 += 1
            
    ct = min(ct0, ct1)
    if ct%2:
        print("DA")
    else:
        print("NET")