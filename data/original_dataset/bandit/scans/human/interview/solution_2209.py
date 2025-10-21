import functools

n = int(input())

arr = [input() for i in range(n)]

def compare(s1, s2):
    a = s1.count('s')
    b = s2.count('s')

    if (a*len(s2)) < b*len(s1):
        return 1
    return -1

arr = sorted(arr, key=functools.cmp_to_key(compare))

s = ''.join(arr)
c = 0
t = 0

for char in s:
    if char == 's':
        c += 1
    elif char == 'h':
        t += c
print(t)