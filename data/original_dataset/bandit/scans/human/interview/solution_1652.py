S = input()
S = "".join(list(reversed(S)))
str_list = ["dream", "dreamer", "erase", "eraser"]
rev_str = []
for i in str_list:
    rev_str.append("".join(list(reversed(i))))
is_OK = True
while len(S) > 0:
    if S[0:5] in rev_str:
        S = S[5:]
    elif S[0:6] in rev_str:
        S = S[6:]
    elif S[0:7] in rev_str:
        S = S[7:]
    else:
        is_OK = False
        break
if is_OK:
    print("YES")
else:
    print("NO")