n = int(input())
len_out, count_in = 0, 0
balance, cur = 0, 0
for c in input():
    if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')) and cur:
        if balance:
            count_in += 1
        else:
            len_out = max(len_out, cur)
        cur = 0
    if c == '(':
        balance += 1
    elif c == ')':
        balance -= 1
    elif ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        cur += 1
if cur:
    len_out = max(len_out, cur)
print(len_out, count_in)