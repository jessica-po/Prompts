N = int(input())
A = [int(_) for _ in input().split()]

def calc(A, y):
    result = abs(A[0] - y)
    t = y
    if t == 0:
        return 10**30
    for a in A[1:N]:
        tt = t + a
        if t * tt >= 0:
            m =  -t // abs(t)
            result += abs(m - tt)
            tt = m
        t = tt
    return result

result = min(calc(A, A[0]), calc(A, -1),  calc(A, +1))

print(result)