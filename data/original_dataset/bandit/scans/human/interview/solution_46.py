ct=0
a, b = list(map(int, input().split(' ')))
x=[0]*5
for i in range(1, b+1):
    x[i%5]+=1
for i in range(1, a+1):
    ct+=x[(0-i)%5]
print(ct)