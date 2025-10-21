from collections import deque
S = input()
mn = [ 300 for i in range( len( S ) ) ]
for i in range( len( S ) - 1, -1, -1 ):
  if i == len( S ) - 1:
    mn[ i ] = ord( S[ i ] )
  else:
    mn[ i ] = min( mn[ i + 1 ], ord( S[ i ] ) )
ans = ""
dq = deque()
for i in range( len( S ) ):
  dq.append( ord( S[ i ] ) )
  while len( dq ) and ( i + 1 == len( S ) or dq[ len( dq ) - 1 ] <= mn[ i + 1 ] ):
    ans += chr( dq[ len( dq ) - 1 ] )
    dq.pop()
print( ans )