def ok(x,y):
    if(len(x)!=len(y)):
        return False
    for i in range(len(x)):
        if(y[i]!='.' and x[i]!=y[i]):
            return False
    return True

n=int(input())

s=input()

L=['Vaporeon', 'Jolteon', 'Flareon', 'Espeon', 'Umbreon', 'Leafeon','Glaceon','Sylveon']


for i in range(len(L)):
    L[i]=L[i].lower()

for item in L:
    if(ok(item,s)):
        print(item)
        break