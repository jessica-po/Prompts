TASK = "stars"
# FIN = open(TASK + ".in")
# FOUT = open(TASK + ".out", "w")

a = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
ans = 0
n = int(input())
if n == 0:
    print(1)
    return
while (n > 0):
    tmp = n % 16
    ans += a[tmp]
    n //= 16

print(ans)

# FIN.close()
# FOUT.close()