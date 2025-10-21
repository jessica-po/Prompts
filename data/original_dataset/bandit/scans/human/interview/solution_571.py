n = q = int(input())
k = list(input())
cntl = k.count('(')
cntr = k.count(')')
cntq = k.count('?')
for i in range(n):
    if k[i] == '?':
        if cntl < q // 2 and cntr + cntq >= q // 2:
            k[i] = '('
            cntl += 1
            cntq -= 1
        else:
            k[i] = ')'
            cntr += 1
            cntq -= 1
        
def check():
    cnt = 0
    m = 0
    for i in k:
        m += 1
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0 and m < n or cnt < 0:
            return False
    return cnt == 0

print(''.join(k) if check() else ':(')