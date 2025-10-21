n = int( input() )
for _ in range( n ):
    s = input()
    i = 0
    a = set()
    while i < len( s ):
        if i == len( s ) - 1 or s[ i ] != s[ i + 1 ]:
            a.add( s[ i ] )
            i += 1
        else:
            i += 2
    l = [ c for c in a ]
    l.sort()
    print( "".join( l ) )