N = input()
X = int(N)
if X % sum(list(map(int, N))) == 0:
    print("Yes")
else:
    print("No")