n,m = map(int, input().split())
A = [0] * n
for i in range(n):
    A[i] = input()
    for j in range(m):
        if A[i][j] == 'S':
            per1,per2 = i,j
            
t1, t2 = per1, per2
end1,end2 = per1,per2
while True:
    
    
    if per1 > 0 and (t1 != per1 - 1 or t2 != per2) and (A[per1-1][per2] == '*' or A[per1-1][per2] == 'S'):
        t1 = per1
        t2 =per2
        per1 -=1
        print('U', end ='')
    elif per1 < n-1 and (t1 != per1 + 1 or t2!= per2) and (A[per1+1][per2] == '*' or A[per1+1][per2] == 'S'):
        t1 = per1
        t2 = per2
        per1 += 1
        print('D', end ='')
    elif per2 > 0 and (t1!=per1 or t2  !=per2 - 1) and (A[per1][per2-1] == '*' or A[per1][per2-1] == 'S'):
        t1 = per1
        t2 = per2
        per2 -=1
        print('L', end ='')
    elif per2 < m -1 and (t1!= per1 or t2 != per2+1) and (A[per1][per2+1] == '*' or A[per1][per2+1] == 'S'):
        t1 = per1
        t2 = per2
        per2 += 1
        print('R', end ='')
    if end1 == per1 and end2 == per2:
        break