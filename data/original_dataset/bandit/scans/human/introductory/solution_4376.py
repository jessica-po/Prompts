d,l = list(map(int,input().split()))

a = list(map(int,input().split()))
letters = list(map(int,input().split()))

pos = [0] * (1+d)

for i,x in enumerate(a):
    pos[i+1] = pos[i] + x

res = []
i = 1
for letter in letters:
    while pos[i]<letter: i+=1
    res.append(str(i) + " " + str(letter - pos[i-1]))
print('\n'.join(res))