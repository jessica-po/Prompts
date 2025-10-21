# You lost the game.
n, a, b = map(int, input().split())
dem = n//2 + n%2
i = 1
while dem > 0 and i <= a:
    dem -= b//2 + (i%2)*(b%2)
    i += 1
if dem > 0:
    print(-1)
else:
    dem = n//2 + n%2
    demo = [2*k+1 for k in range(dem)]
    rep = [2*k for k in range(1,n//2+1)]
    d = 0
    r = 0
    l = 0
    for i in range(a):
        l = 1-l
        e = l
        for j in range(b):
            if e and d < dem:
                print(demo[d],end=" ")
                d += 1
            elif e == 0 and r < n//2:
                print(rep[r],end=" ")
                r += 1
            else:
                print(0,end=" ")
            e = 1-e
        print()