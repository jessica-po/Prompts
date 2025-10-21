a,b,c,d = map(int,input().split())
ab = a + b
cd = c + d
if ab > cd:
    print('Left')
elif ab < cd:
    print('Right')
else:
    print('Balanced')