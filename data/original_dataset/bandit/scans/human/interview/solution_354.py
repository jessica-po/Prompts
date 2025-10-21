v = list('aeiou')
s = [c in v for c in input()]
t = [c in v for c in input()]
if s == t:
    print('Yes')
else:
    print('No')