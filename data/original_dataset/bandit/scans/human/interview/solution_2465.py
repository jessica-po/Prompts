def gcd(a,b):
  return a if b==0 else gcd(b, a%b)

for T in range(int(input())):
  de=int(input())
  g=gcd(de, 180)
  if int(de/g)==int(180/g)-1:
    print(int(180/g)*2)
  else:
    print(int(180/g))