# You lost the game.

n = int(input())
L = list(map(int, input().split()))

if n == 1:
    if L[0] == 0:
        print("UP")
    elif L[0] == 15:
        print("DOWN")
    else:
        print("-1")
else:
    d = L[n-2] - L[n-1]
    if d < 0:
        if L[n-1] == 15:
            print("DOWN")
        else:
            print("UP")
    else:
        if L[n-1] == 0:
            print("UP")
        else:
            print("DOWN")