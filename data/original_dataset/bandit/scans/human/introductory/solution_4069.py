x, k, d = map(int, input().split())
if x < 0:
    x *= -1
cnt = min(k, x//d+1)
x -= cnt * d
if abs(x) < x+d:
    x += d
    cnt -= 1
    x -= d * ((k-cnt)%2)
else:
    x += d * ((k-cnt)%2)
print(abs(x))