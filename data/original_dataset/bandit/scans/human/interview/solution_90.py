fact = [ 1 ]
for i in range( 1, 20, 1 ):
  fact.append( fact[ i - 1 ] * i )

from collections import defaultdict

N, K, S = list(map( int, input().split() ))
A = list( map( int, input().split() ) )

ldp = [ [ defaultdict( int ) for i in range( K + 1 ) ] for j in range( 2 ) ]
ldp[ 0 ][ 0 ][ 0 ] = 1
for i in range( N // 2 ):
  for j in range( K + 1 ):
    ldp[ ~ i & 1 ][ j ].clear()
  for j in range( K + 1 ):
    for key in ldp[ i & 1 ][ j ]:
      ldp[ ~ i & 1 ][ j ][ key ] += ldp[ i & 1 ][ j ][ key ] # toranai
      ldp[ ~ i & 1 ][ j ][ key + A[ i ] ] += ldp[ i & 1 ][ j ][ key ] # toru
      if j + 1 <= K and A[ i ] <= 18:
        ldp[ ~ i & 1 ][ j + 1 ][ key + fact[ A[ i ] ] ] += ldp[ i & 1 ][ j ][ key ] # kaijyou totte toru

rdp = [ [ defaultdict( int ) for i in range( K + 1 ) ] for j in range( 2 ) ]
rdp[ 0 ][ 0 ][ 0 ] = 1
for i in range( N - N // 2 ):
  for j in range( K + 1 ):
    rdp[ ~ i & 1 ][ j ].clear()
  for j in range( K + 1 ):
    for key in rdp[ i & 1 ][ j ]:
      rdp[ ~ i & 1 ][ j ][ key ] += rdp[ i & 1 ][ j ][ key ]
      rdp[ ~ i & 1 ][ j ][ key + A[ N // 2 + i ] ] += rdp[ i & 1 ][ j ][ key ]
      if j + 1 <= K and A[ N // 2 + i ] <= 18:
        rdp[ ~ i & 1 ][ j + 1 ][ key + fact[ A[ N // 2 + i ] ] ] += rdp[ i & 1 ][ j ][ key ]

ans = 0
for i in range( K + 1 ):
  for key in ldp[ N // 2 & 1 ][ i ]:
    for j in range( 0, K - i + 1, 1 ):
      ans += ldp[ N // 2 & 1 ][ i ][ key ] * rdp[ N - N // 2 & 1 ][ j ][ S - key ]

print( ans )