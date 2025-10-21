s = input()
a, b = s.count('x'), s.count('y')
if b > a: print('y' * (b - a))
else: print('x' * (a - b))