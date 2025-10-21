n = int(input())

m = 6
arr = []
for i in range(n):
    arr.append(input())
    
for i in range(n - 1):
    for j in range(i + 1, n):
        d = 0
        for z in range(6):
            if arr[i][z] != arr[j][z]:
                d += 1
                
        if d == 6:
            m = min(m, 2)
        elif d == 5:
            m = min(m, 2)
        elif d == 4:
            m = min(m, 1)
        elif d == 3:
            m = min(m, 1)
        else:
            m = 0
            
print(m)