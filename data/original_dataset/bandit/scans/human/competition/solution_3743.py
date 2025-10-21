n = int(input())
p = 2
while n % p and p ** 2 <= n:
    p += 1
if p ** 2 > n:
    p = n
pw = n.bit_length() // p.bit_length()
while pow(p, pw) < n:
    pw += 1
while pow(p, pw) > n:
    pw -= 1
if pow(p, pw) == n:
    print(p)
else:
    print(1)