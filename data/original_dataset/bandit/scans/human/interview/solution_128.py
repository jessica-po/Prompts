# You lost the game.
n,k = map(int, input().split())
r = 0
for i in range(min(k,n//2)):
    r += (n-2*i-1) + (n-2*i-2)
print(r)