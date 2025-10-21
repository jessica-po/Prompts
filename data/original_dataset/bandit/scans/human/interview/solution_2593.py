t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    counts = [0] * 32
    for x in a:
        counts[len(bin(x))-2] += 1
        
    total = 0
    for count in counts:
        total += count * (count-1) // 2
    print(total)