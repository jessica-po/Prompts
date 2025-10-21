try:
    r, c = map(int, input().split())
    mat = []
    for i in range(r):
        arr=list(map(int, input().split()))
        mat.append(arr)
    flag=0
    arr1=[]
    for x in range(c):
        arr = []
        for j in range(r):
            arr.append(mat[j][x])
        arr1.append(arr)
    i=0
    for i in range(r):
        for j in range(c):
            if mat[i][j]==max(arr1[j]) and mat[i][j]==min(mat[i]):
                flag=1
                print(mat[i][j])
                break
        if flag==1:
            break
    if flag==0:
        print("GUESS")
except:
    pass