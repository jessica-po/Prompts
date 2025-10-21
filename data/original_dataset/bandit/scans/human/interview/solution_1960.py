N = int( input() )
A = list( map( int, input().split() ) )

maxa = max( A )

def upd( ftree, x, v ):
  while x <= maxa:
    ftree[ x ] = max( ftree[ x ], v )
    x += x & -x

def qry( ftree, x ):
  res = 0
  while x:
    res = max( res, ftree[ x ] )
    x -= x & -x
  return res

st_len = [ 0 for i in range( N ) ]
ftree = [ 0 for i in range( maxa + 1 ) ]
for i in range( N - 1, -1, -1 ):
  st_len[ i ] = qry( ftree, maxa + 1 - A[ i ] - 1 ) + 1
  upd( ftree, maxa + 1 - A[ i ], st_len[ i ] )

ed_len = [ 0 for i in range( N ) ]
ftree = [ 0 for i in range( maxa + 1 ) ]
for i in range( N ):
  ed_len[ i ] = qry( ftree, A[ i ] - 1 ) + 1
  upd( ftree, A[ i ], ed_len[ i ] )

max_len = max( st_len )
st_cnt_len = [ 0 for i in range( N + 1 ) ]
for i in range( N ):
  if ed_len[ i ] + st_len[ i ] - 1 == max_len:
    st_cnt_len[ st_len[ i ] ] += 1

for i in range( N ):
  if ed_len[ i ] + st_len[ i ] - 1 != max_len:
    print( 1, end = "" )
  elif st_cnt_len[ st_len[ i ] ] > 1:
    print( 2, end = "" )
  else:
    print( 3, end = "" )
print()