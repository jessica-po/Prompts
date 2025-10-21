from sys import stdin, stdout, exit

mod = 10**9 + 7

def modinv(x):
    return pow(x, mod-2, mod)

N = 2*10**5 + 10
facts = [1]*N
for i in range(1,N):
    facts[i] = facts[i-1] * i
    facts[i] %= mod

def binom(n, k):
    ans = modinv(facts[k]) * modinv(facts[n-k])
    ans %= mod
    ans *= facts[n]
    ans %= mod
    return ans

#print("Finished preprocess")

n, T = list(map(int, stdin.readline().split()))
ts = list(map(int, stdin.readline().split()))

ans = 0
total = sum(ts)
running = total
last_idx = n-1
while running > T:
    running -= ts[last_idx]
    last_idx -= 1
#print(last_idx+1)

last_bd = -1
last_sum = 0
idx = last_idx
while running + idx + 1 > T:
    bd = T - running
#    print("time remaining for", idx+1, "flips is", bd)
    cur_sum = last_sum + (binom(idx+1, last_bd) if last_bd >= 0 else 0)
    cur_sum *= modinv(2)
    cur_sum %= mod
    for fresh in range(last_bd+1, bd+1):
        cur_sum += binom(idx+1, fresh)
        cur_sum %= mod
 #   print("pr of", idx+1, "flips is", cur_sum, cur_sum / (2**(idx+1)))
    ans += cur_sum * modinv(pow(2, idx+1, mod))
    ans %= mod
    running -= ts[idx]
    last_bd = bd
    last_sum = cur_sum
    idx -= 1

#print(idx+1, "freebies")
ans += idx+1
ans %= mod
print(ans)