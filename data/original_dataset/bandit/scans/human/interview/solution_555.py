x = list(input())

for i in range(len(x)):
    if(i==0 and x[i]=='9'):
        continue
    if(int(x[i])>9-int(x[i])):
        x[i] = str(9-int(x[i]))
y=0
for item in x:
    y*=10
    y+=int(item)
print(y)