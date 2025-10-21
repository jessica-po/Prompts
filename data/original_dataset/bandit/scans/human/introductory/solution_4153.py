s =input()

from collections import Counter
count = Counter(s)
c0 = count["0"]
c1 = count["1"]

print(min(c0,c1)*2)