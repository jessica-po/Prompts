def S(n):
    c = 0
    for i in range(len(n)):
        c += int(n[i])
    return c
 
N = input()
if int(N) % S(N) == 0:
    print('Yes')
else:
    print('No')