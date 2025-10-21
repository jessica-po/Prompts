a, b = map(int, input().split())

if a <= b:
    ans = str(a) * b
else:
    ans = str(b) * a
print(ans)
return