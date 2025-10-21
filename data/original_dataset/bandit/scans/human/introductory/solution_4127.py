a, b = input().split()
a = int(a)
b1, b2 = b.split('.')
b3 = int(b1)*100 + int(b2)

print((a*b3//100))