a,b,mod = list(map(int, input().split()))

g = [2] * a
for i in range(b):
    t = input()
    for x, y in  enumerate(t):
        if y == '1':
            g[x] -= 1

one = two = 0
for q in g:
    if q < 0:
        print(0)
        return

    if q == 1:
        one+=1
    if q == 2:
        two+=1



mat = [[0]*600 for x in range(600)]  
mat[0][0] = 1
#int(one, two)
for j in range(a + 1):
    for i in range(a + 1):
        if i-2>=0:
            mat[i][j] += i*(i-1) // 2 * mat[i-2][j];
            #print('in',i,j, mat[i][j], i*(i-1)//2, mat[i-2][j], i-2, mat[0][0])
        if j-1>=0:
            mat[i][j] += i*j * mat[i][j -1];
        if j-2>=0 :
            mat[i][j] += j *(j-1)//2 * mat[i+2][j -2];
        mat[i][j] %= mod

#print(mat[2][0])
#print(mat[0][2])
print(mat[one][two])