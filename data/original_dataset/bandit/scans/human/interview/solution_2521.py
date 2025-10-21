import heapq

data = int(input())
array = [int(_) for _ in input().split()]

X = array[0:data]
B = array[data:2*data]
Y = [-_ for _ in array[2*data:3*data]]

heapq.heapify(X)
heapq.heapify(Y)

x = [sum(X)]
y = [sum(Y)]

for i in range(data):
    x += [B[i] - heapq.heappushpop(X, B[i])]
    y += [-B[-1-i] - heapq.heappushpop(Y, -B[-1-i])]

for i in range(data):
    x[i+1] = x[i]+x[i+1]
    y[i+1] = y[i]+y[i+1]

print(max([x[_] + y[-1 - _] for _ in range(data+1)]))