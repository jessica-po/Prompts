n = int(input())
a = input()
prot = dict()
prot["D"] = "U"
prot["L"] = "R"
prot["R"] = "L"
prot["U"] = "D"
was = set()
ans = 1
for i in range(n):
    if (a[i] not in was):
        if (len(was) == 0):
            was.add(a[i])
        elif len(was) == 1:
            if (prot[a[i]] not in was):
                was.add(a[i])
            else:
                was.clear()
                was.add(a[i])
                ans += 1
        else:
            was.clear()
            was.add(a[i])
            ans += 1
print(ans)