#!/usr/bin/python
a = input()
x='iloveyou'
for i in x:
 if i not in a:
  print("sad")
  return
if a.count('o') < 2:
 print("sad")
 return
print("happy")
return