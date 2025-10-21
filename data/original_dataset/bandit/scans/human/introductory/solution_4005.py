x1, y1, x2, y2 = list(map( int, input().split() ))
x3, y3, x4, y4 = list(map( int, input().split() ))
x5, y5, x6, y6 = list(map( int, input().split() ))

covered = False
if x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2:
    covered = True
elif x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2:
    covered = True
elif x1 >= x3 and x1 >= x5 and x2 <= x4 and x2 <= x6:
    if min( y4, y6 ) >= max( y3, y5 ) and min( y3, y5 ) <= y1 and max( y4, y6 ) >= y2:
        covered = True
elif y1 >= y3 and y1 >= y5 and y2 <= y4 and y2 <= y6:
    if min( x4, x6 ) >= max( x3, x5 ) and min( x3, x5 ) <= x1 and max( x4, x6 ) >= x2:
        covered = True

print( "NO" if covered else "YES" )