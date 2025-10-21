from itertools import *

inStr=next(open('input.txt'))
n=int(inStr.split()[0])
m=int(inStr.split()[1])


boys=repeat('B', n)
girls=repeat('G', m)

if n>m:
    pairs = zip_longest(boys, girls)
else:
    pairs = zip_longest(girls, boys)
result = (y for x in pairs for y in x if y is not None)
ans = ''.join(result)
open('output.txt', 'w').write(ans)
print(ans)