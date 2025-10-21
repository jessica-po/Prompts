n = int( input() )
s = input()
d = 0
l = []
for c in s:
    if c == '(':
        l.append(d)
        d ^= 1
    else:
        d ^= 1
        l.append( d )

print( "".join( [ str(i) for i in l ]))