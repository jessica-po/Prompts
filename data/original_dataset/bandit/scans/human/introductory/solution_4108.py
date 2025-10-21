S = input()
T = input()

s = [[] for i in range(26)]
t = [[] for i in range(26)]

for i in range(len(S)):
    s[ord(S[i])-97].append(i)
    t[ord(T[i])-97].append(i)

s = sorted(s)
t = sorted(t)
if s == t:
    print("Yes")
else:
    print("No")