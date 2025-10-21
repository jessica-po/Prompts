t = int(input())

for _ in range(t):
    p = sorted(input())
    h = input()
    
    for i in range(len(h)-len(p)+1):
        if sorted(h[i:i+len(p)])==p:
            print("YES")
            break
    else:
        print("NO")