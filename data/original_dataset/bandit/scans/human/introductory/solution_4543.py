#ABC086B
a,b = input().split()
a += b
a = int(a)
print("Yes" if int((a**.5))**2 == a else "No")