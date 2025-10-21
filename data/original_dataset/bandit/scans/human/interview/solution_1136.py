import math
MOD = int( 1e9 + 7 )

N, M = map( int, input().split() )
sn = int( math.sqrt( N ) )

ans = N * M % MOD
for i in range( 1, min( sn, M ) + 1, 1 ):
  ans -= N // i * i

ans %= MOD
if N // ( sn + 1 ) > M:
  exit( print( ans ) )

for f in range( N // ( sn + 1 ), 0, -1 ):
  s = lambda x: x * ( x + 1 ) // 2
  if N // f > M:
    ans -= f * ( s( M ) - s( N // ( f + 1 ) ) )
    break
  ans -= f * ( s( N // f ) - s( N // ( f + 1 ) ) )

ans %= MOD
if ans < 0:
  ans += MOD
print( ans )