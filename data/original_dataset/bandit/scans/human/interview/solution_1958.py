n,p = list(map(int,input().split()))
temp = [input() for i in range(n)]
num = 0
num2 = 0
for i in range(n-1,-1,-1):
    if temp[i] == "halfplus":
        num *= 2
        num += 1
        num2 += num/2*p
    else:
        num2 += num*p
        num *= 2
print(int(num2))