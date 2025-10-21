# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
ar=[]
for i in range(0,n):
    s=input()
    t=re.search(r"^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)
    if t:
        ar.append(s)
ar.sort()        
print(ar)