H, W = map(int, input().split())
s = '#' * (W + 2)
data = []
data.append(s)
for i in range(H):
    data.append('#' + str(input()) + '#')
data.append(s)
   
for i in range(H + 2):
    print(data[i])