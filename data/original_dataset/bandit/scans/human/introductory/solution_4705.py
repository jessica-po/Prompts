# １食８００円をN食食べた
N = int( input() )
x = int( 800 * N )

#  １５食食べるごとに２００円もらえる

y = N // 15 * 200

print( x - y )