n = int(input())
A = input()
x = A.count('G')
num_1 = 0
num_2 = 0
max_num = 0
flag = 0
for i in range(n):
    if A[i] == 'G' and flag == 0:
        num_1 += 1
    elif A[i] == 'G' and flag == 1:
        num_2 += 1
    elif A[i] == 'S' and flag == 0:
        flag = 1
    else:
        if num_1 + num_2 + 1 <= x:
            if num_1 + num_2 + 1 > max_num:
                max_num = num_1 + num_2 + 1
            num_1 = num_2
            num_2 = 0
            flag = 1
        else:
            if num_2 + num_1 > max_num:
                max_num = num_1 + num_2
            num_1 = num_2
            num_2 = 0
            flag = 1
if num_1 + num_2 + 1 <= x:
    if num_1 + num_2 + 1 > max_num:
        max_num = num_1 + num_2 + 1
else:
    if num_2 + num_1 > max_num:
        max_num = num_1 + num_2
print(max_num)