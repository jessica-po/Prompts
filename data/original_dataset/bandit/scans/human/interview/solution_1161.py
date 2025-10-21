seq = input()
a = []
fl = True
z = 0
for i in seq:
    if i == '<' or i == '[' or i == '{' or i == '(':
        a.append(i)
    elif i == '>':
        if len(a) and a[-1] == '<': a.pop()
        elif len(a) and a[-1] != '<':
            a.pop()
            z += 1
        else:
            fl = False
            break
    elif i == ')':
        if len(a) and a[-1] == '(': a.pop()
        elif len(a) and a[-1] != '(':
            a.pop()
            z += 1
        else:
            fl = False
            break
    elif i == ']':
        if len(a) and a[-1] == '[': a.pop()
        elif len(a) and a[-1] != '[':
            a.pop()
            z += 1
        else:
            fl = False
            break
    elif i == '}':
        if len(a) and a[-1] == '{': a.pop()
        elif len(a) and a[-1] != '{':
            a.pop()
            z += 1
        else:
            fl = False
            break
if len(a): fl = False
if fl: print(z)
else: print('Impossible')