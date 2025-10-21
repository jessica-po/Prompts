input()
s = input()

if 'MM' in s or 'YY' in s or 'CC' in s:
    print ('No')
elif s.startswith('?') or s.endswith('?'):
    print ('Yes')
elif '??' in s:
    print ('Yes')
elif 'C?C' in s or 'M?M' in s or 'Y?Y' in s:
    print ('Yes')
else:
    print ('No')