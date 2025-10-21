s= input()
color = "chokudai"
d = []

for c in s:
    if c != color:
        d.append(c)
        color = c
print(len(d)-1)