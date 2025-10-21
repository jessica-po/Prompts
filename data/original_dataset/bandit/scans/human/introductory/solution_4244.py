import numpy as np
N = int(input())
Xi = list(map(int, input().split()))
Xi = np.array(Xi)
min = float('inf')
for i in range(1, 101):
    tmp = np.sum(np.square(Xi - i))
    if tmp < min:
        min = tmp
print(min)