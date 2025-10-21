s = input()
t = input()
l, r = [0]*len(t), [0]*len(t)
li, ri = 0, len(s) - 1
for i in range(len(t)):
    while s[ li ] != t[ i ]:
        li += 1
    while s[ ri ] != t[ - i - 1 ]:
        ri -= 1
    l[ i ] = li
    r[ -i -1 ] = ri
    li += 1
    ri -= 1

print( max( [ r[ 0 ], len(s) - l[ -1 ] - 1 ] + [ max( 0, r[ i ] - l[ i - 1 ] ) - 1 for i in range( 1, len(t) ) ] ) )