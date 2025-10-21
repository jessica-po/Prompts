a, b = list(map(int, input().split(' ')))
c, d = list(map(int, input().split(' ')))
e, f = list(map(int, input().split(' ')))
x=[[a, b],[c,d],[e,f]]
x.sort()
a, b, c, d, e, f = x[0][0], x[0][1], x[1][0], x[1][1], x[2][0], x[2][1]
if (a==c==e or b==d==f):
    print(1)
    quit()

if a == c:
    if b<f<d:
        print(3)
        quit()
    print(2)
    quit()

if c == e:
    if (d<b<f):
        print(3)
        quit()
    print(2)
    quit()

if b == d:
    print(2)
    quit()

if d == f:
    print(2)
    quit()

if b == f:
    if a<c<e:
        print(3)
        quit()
    print(2)
    quit()

print(3)
quit()