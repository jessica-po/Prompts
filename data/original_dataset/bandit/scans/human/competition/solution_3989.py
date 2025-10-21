def end(x) :
    if x == 0 :
        return "1869";
    if x == 6 :
        return "1968";
    if x == 5 :
        return "1689";
    if x == 4 :
        return "6891";
    if x == 3 :
        return  "1689";
    if x == 2 :
        return  "1986";
    if x == 1 :
        return  "1896";

d = [0] * 10;
for c in input() :
    d[int(c)] += 1;
for i in [1,6,8,9] :
    d[i] -= 1;

s = "";
ost = 0;

for i in range(10) :
    for j in range(d[i]):
        ost = (ost * 10 + i) % 7;

ost = (1869, 1896, 1986, 1698, 6198, 1689, 1968)[ost * 10000 % 7];

for c in (1,2,3,4,5,6,7,8,9) :
    s += str(c) * d[c];

print((s + str(ost) + "0" * d[0]));