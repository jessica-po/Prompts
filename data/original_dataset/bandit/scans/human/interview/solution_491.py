n = int(input())
if n >= 0:
    print(n)
else:
    n = str(n)
    print(max(int(n[:-1]), int(n[:-2] + n[-1])))