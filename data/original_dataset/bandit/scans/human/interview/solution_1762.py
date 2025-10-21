# tested by Hightail - https://github.com/dj3500/hightail


from heapq import heappop, heappush
from sys import stdin, stdout


read, read_array = stdin.readline, lambda: stdin.readline().split()
write = lambda *args, **kw: stdout.write(kw.get('sep', ' ').join(str(a) for a in args) + kw.get('end', '\n'))
write_array = lambda arr, **kw: stdout.write(kw.get('sep', ' ').join(str(a) for a in arr) + kw.get('end', '\n'))
read_int, read_int_array = lambda: int(read()), lambda: [int(p) for p in read_array()]
read_float, read_float_array = lambda: float(read()), lambda: [float(p) for p in read_array()]


n, k = read_int_array()
heap = []
busy = 0
time = 0
finish = [0] * n
for i in range(n):
    if busy == k:
        time = heappop(heap)
        busy -= 1
    else:
        time = 0
    start, minutes = read_int_array()
    if start > time:
        time = start
    heappush(heap, time + minutes)
    finish[i] = time + minutes
    busy += 1

write_array(finish, sep='\n')