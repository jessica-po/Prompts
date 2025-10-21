X,Y = list(map(int,input().split()))
#X, 2X, 4X,...,2^(t-1)*X<=Yとなる最大のt
#10^18 はだいたい2^60だから全部試せそう
for t in range(1,100):
    if 2**(t-1)*X<=Y:
        out = t
    else:
        break
print(out)