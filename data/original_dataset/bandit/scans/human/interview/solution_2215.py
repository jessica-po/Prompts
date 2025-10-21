n, m = map(int, input().split())
ans = ["0"] * n
for i in range(1, n, 2):
    ans[i] = "1"
print("".join(ans))