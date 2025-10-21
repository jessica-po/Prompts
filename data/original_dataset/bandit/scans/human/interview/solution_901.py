n, m = map(int,input().split())
for i in range(m):
    a, *b = map(int,input().split())
    b = set(b)
    for j in b:
        if -j in b:
            break
    else:
        print("YES")
        break
else:
    print("NO")