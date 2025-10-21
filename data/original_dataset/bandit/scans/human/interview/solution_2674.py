n = input()
ans = 0
for i in n:
    ans = ans ^int(i)
if ans:
    print("Inclusive")
else:
    print("Exclusive")