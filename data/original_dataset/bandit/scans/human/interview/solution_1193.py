n, k = map(int, input().split())
s = sorted(list(map(int, input().split())), reverse = True)
print(s[k - 1])