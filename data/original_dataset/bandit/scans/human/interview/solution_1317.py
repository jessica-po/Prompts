s = input().split()
n, m = int(s[0]), int(s[1])
qr = {}
for i in range(1, m+1):
    num = (n-i)//m+1
    qr[(i**2)%m] = qr.get((i**2)%m,0)+ num
print(sum(qr.get(i%m,0) * qr.get((m-i)%m,0) for i in range(m)))