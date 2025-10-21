a = []
b = []
x = input()
for i in range(len(x)-1):
    if x[i]+x[i+1] == 'AB':
        a.append(i)
    elif x[i]+x[i+1] == 'BA':
        b.append(i)

if a == [] or b == []:
    print("NO")
    quit()
    
if abs(min(a)-max(b))>1 or abs(max(a)-min(b))>1:
    print("YES")
    quit()
print("NO")