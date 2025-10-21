s=[]
s.append("qwertyuiop")
s.append("asdfghjkl;")
s.append("zxcvbnm,./")

x=input()
y=input()

for item in y:
    for i in range(3):
        for j in range(len(s[i])):
            if(s[i][j]==item):
                if(x=='R'):
                    print(s[i][j-1],end="")
                else:
                    print(s[i][j+1],end="")
print()