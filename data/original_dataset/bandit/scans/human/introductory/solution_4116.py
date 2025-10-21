import sys
 
n = int(input())
 
for a in range(1,10):
    if n % a == 0 and n // a <= 9:
        print("Yes")
        return
print("No")