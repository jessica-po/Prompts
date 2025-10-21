import numpy as np

N, *AB = list(map(int, open(0).read().split()))
min_med = np.median([a for a in AB[::2]])
max_med = np.median([b for b in AB[1::2]])
if N % 2:
    print((int(max_med - min_med) + 1))
else:
    print((int(max_med * 2 - min_med * 2) + 1))