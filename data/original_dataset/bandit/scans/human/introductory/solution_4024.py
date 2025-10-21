import sys
import itertools

inputs = sys.stdin.read().split()
len_string = int(inputs[0])
desired_size = int(inputs[1])
string = inputs[2]

size = 0
cost = 0
cur_set = set()
cur_set.add(string)
for i in range(len_string, -1, -1):
    cur_size = len(cur_set)
    if size+cur_size >= desired_size:
        cost += (desired_size-size)*(len_string-i)
        size = desired_size
        break
    cost += cur_size*(len_string-i)
    size += cur_size
    
    new_set = set()
    for substr in cur_set:
        for i in range(len(substr)):
            new_set.add(substr[:i]+substr[(i+1):])
    cur_set = new_set

if size >= desired_size: sys.stdout.write(str(cost)+"\n")
else: sys.stdout.write("-1\n")