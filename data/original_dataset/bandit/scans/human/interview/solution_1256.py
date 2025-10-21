s = input()
l = [int(x) for x in s.split('+')]
l.sort()
print('+'.join([str(x) for x in l]))