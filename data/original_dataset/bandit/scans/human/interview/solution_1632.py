MAX_N = 5001

a = [0] * MAX_N;
raz = [0] * (MAX_N + 10);
s = [0] * (MAX_N + 10);

n = int(input())

a = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if a[i] - a[j] > 0:
            raz[a[i] - a[j]] += 1


for i in range(1, MAX_N + 1):
     s[i] = s[i - 1] + raz[i]
     
ans = 0;

for i in range(1, MAX_N):
    if raz[i] == 0:
        continue
    for j in range(1, MAX_N):
        if i + j > MAX_N:
            break
        if raz[j] == 0:
            continue
        ans += raz[i] * raz[j] * (s[MAX_N] - s[i + j])

ans = ans * 1.0
ans /= s[MAX_N]
ans /= s[MAX_N]
ans /= s[MAX_N]

print(ans)