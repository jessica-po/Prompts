n = [ int(i) for i in  input().split() ]
p = [ int(i) for i in input().split() ]

p = sorted(p)
val = sum( p[:n[1]] )
print(val)