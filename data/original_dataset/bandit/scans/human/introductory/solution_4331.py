N=int(input())
X=N%10
y=N//10
Y=y%10
Z=N//100
if X==7 or Y==7 or Z==7:
  print("Yes")
else:
  print("No")