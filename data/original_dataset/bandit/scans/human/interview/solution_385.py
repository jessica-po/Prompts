n, m, p = [int(x) for x in input().split()]
A = input().rstrip()
B = input().rstrip()

pair = [0] * n
stack = []
for (i, c) in enumerate(A):
    if c == '(':
        stack.append(i)
    else:
        j = stack.pop()
        pair[i] = j
        pair[j] = i

start = 0
pointer = p - 1
left = list(range(-1, n-1))
right = list(range(1, n+1))
left[0] = None
right[-1] = None

for c in B:
    if c == 'R':
        pointer = right[pointer]
    elif c == 'L':
        pointer = left[pointer]
    else:
        if pair[pointer] < pointer:
            if right[pointer] is not None:
                left[right[pointer]] = left[pair[pointer]]
            if left[pair[pointer]] is not None:
                right[left[pair[pointer]]] = right[pointer]
            else:
                start = right[pointer]

            if right[pointer] is None:
                pointer = left[pair[pointer]]
            else:
                pointer = right[pointer]
        else:
            if right[pair[pointer]] is not None:
                left[right[pair[pointer]]] = left[pointer]
            if left[pointer] is not None:
                right[left[pointer]] = right[pair[pointer]]
            else:
                start = right[pair[pointer]]


            if right[pair[pointer]] is None:
                pointer = left[pointer]
            else:
                pointer = right[pair[pointer]]

i = start
while right[i] is not None:
    print(A[i], end = '')
    i = right[i]
print(A[i])