import re

s = input()
ops = re.split('([+-])', s)
assert len(ops) % 2 == 1
ops = ['+'] + ops

total = 0
for i in range(0, len(ops), 2):
    if ops[i] == '+':
        total += int(ops[i+1])
    elif ops[i] == '-':
        total -= int(ops[i+1])
    else:
        assert False

for b in bytes(str(total), 'ascii'):
    print('+' * b + '.>')