t = int(input())
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for i in range(t):
    a, b, q = map(int, input().split())
    z = gcd(a, b)
    target = (a * b)//z
    pref = [0]
    for j in range(1, target + 1):
        if (j%a)%b != (j%b)%a:
            pref.append(pref[-1]+1)
        else:
            pref.append(pref[-1])
    
    result = []
    for i in range(q):
        l , r = map(int, input().split())
        temp_r = (r//target) * pref[-1]
        r = r%target
        l -= 1
        temp_l = (l//target) * pref[-1]
        l = l%target
        temp_r += pref[r]
        temp_l += pref[l]
        result.append(temp_r - temp_l)
    print(*result)