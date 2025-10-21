s = input()
q = set()
for i in range(0, len(s)):
    q.add(s[i])
print("IGNORE HIM!" if len(q) % 2 == 1 else "CHAT WITH HER!")