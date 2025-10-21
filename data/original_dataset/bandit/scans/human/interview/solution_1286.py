k = int(input())
MOD = 10 ** 9 + 7
antithree = pow(3, MOD - 2, MOD)
antitwo = pow(2, MOD - 2, MOD)
power = 1
parity = False
for t in map(int, input().split()):
    power *= t
    power %= MOD - 1
    if t % 2 == 0:
        parity = True
q = pow(2, power, MOD) * antitwo
q %= MOD
if parity:
    p = (q + 1) * antithree
    p %= MOD
else:
    p = (q - 1) * antithree
    p %= MOD    
print(p, q, sep = '/')