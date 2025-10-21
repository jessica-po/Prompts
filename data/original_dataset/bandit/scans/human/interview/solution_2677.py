s = input()
L = []

for i in s:
 L.append(i)

vowels = ['A', 'E', 'I', 'O', 'U']

flag = 0
for i in range(len(L)-2):
 if (L[i] in vowels) and (L[i+1] in vowels) and (L[i+2] in vowels):
  flag = 1
  break
if flag == 1:
 while 'A' in L:
  L.remove('A')

 while 'E' in L:
  L.remove('E')

 while 'I' in L:
  L.remove('I')

 while 'O' in L:
  L.remove('O')

 while 'U' in L:
  L.remove('U')

 newL = []

 for i in L:
  if i not in newL:
   newL.append(i)

 if len(newL) >= 5:
  print("GOOD")
 else:
  print(-1)
else:
 print(-1)