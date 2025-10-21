ct = 0
x = int(input())
y = int(input())
z = [int(input()) for i in range(x)]
z.sort()
z.reverse()
for i in z:
    if y <= 0:
        print(ct)
        quit()
        
    y-=i
    ct+=1
print(ct)