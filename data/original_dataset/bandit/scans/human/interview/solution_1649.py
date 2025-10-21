A,B,C,D=list(map(int,input().split()))
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                sum1 = 0
                sum2 = 0
                if i == 1:
                    sum1 += A
                else:
                    sum2 += A
                if j ==1:
                    sum1 += B
                else:
                    sum2 += B
                if k == 1:
                    sum1 += C
                else:
                    sum2 += C
                if l == 1:
                    sum1 += D
                else:
                    sum2 += D
                if sum1 == sum2:
                    print("Yes")
                    return
print("No")