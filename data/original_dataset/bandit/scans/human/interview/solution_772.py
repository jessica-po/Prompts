a = []
b = []
for i in range(3):
      t =  input().split() 
      a.append([int(t[0]), int(t[1]), int(t[2]) ] )
      b.append([1, 1, 1])

def add(i, j, w):
      if 2>=i>=0 and 2>=j>=0:
            b[i][j] += w

for i in range(3):
      for j in range(3):
            add(i, j, a[i][j])
            add(i-1, j, a[i][j])
            add(i+1, j, a[i][j])
            add(i, j+1, a[i][j])
            add(i, j-1, a[i][j])

for i in range(3):
      print( ''.join( map(str, [ [0,1][b[i][j]%2 ] for j in range(3) ] ) ) )