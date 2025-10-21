n = int(input())
u, v, f, B = 1, 1 , 1, 10**9+7
for i in range(2,n+2):
    u  = u * i % B
for i in range(2,n+n+3):
    f  = f * i % B
def inv(u):
    if u < 2:
        return 1
    return (-(B // u) * inv(B % u)) % B

print((f * inv(u) * inv(u) + B - 1) % B)